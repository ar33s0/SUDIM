from playwright.sync_api import sync_playwright
from rich.console import Console
import sys
import os

console = Console()

def get_data(number_phone):

    if not(os.path.exists('browsers/splus_browser')): 
        return('[red]The splus_browser Folder Not Exists Please First Run "login.py"[/red]')
        sys.exit()

    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/splus_browser',
            headless=False,
            executable_path='/usr/bin/chromium',
            viewport={'width': 1920, 'height': 1080},
            #no_viewport=True
        )

        # fix for splus
        edited_number_phone = "+98" + number_phone
        #console.print('[bright_green]Adding...[/bright_green]')
        page = context.new_page()

        page.goto('https://web.splus.ir')
        page.click('.bottomTabs .tab:has-text("حساب من")')
        page.click('text="مخاطبین"')
        page.click('[aria-label="مخاطب جدید"]')
        page.wait_for_timeout(1000)
        page.fill('[aria-label="شماره تلفن"]', edited_number_phone)
        page.fill('[aria-label="نام (الزامی)"]', edited_number_phone)
        page.wait_for_timeout(1000)
        page.click('.confirm-dialog-button:has-text("تأیید")', force=True)

        try: 
            page.locator('text="این شخص بااین شماره تلفن هنوز در سروش پلاس ثبت نام نکرده است"').wait_for(state='attached', timeout=3000)
            return('\n[red]It Doesnt Have Splus.[/red]')
        except:
            pass

        # for caution
        try:
            page.wait_for_timeout(500)
            page.click('[aria-label="ویرایش"]')
            page.click('text="حذف مخاطب"')
            page.wait_for_timeout(1000)
            page.locator('.Button.confirm-dialog-button:has-text("حذف مخاطب")').nth(0).click()
            page.wait_for_timeout(500)
        except Exception as e:
            while_counter = 0
            while while_counter < 5: 
                try: 
                    while_counter += 1
                    page.reload()
                    page.click('[aria-label="مخاطب جدید"]')
                    page.wait_for_timeout(1000)
                    page.fill('[aria-label="شماره تلفن"]', edited_number_phone)
                    page.fill('[aria-label="نام (الزامی)"]', edited_number_phone)
                    page.wait_for_timeout(1000)
                    page.click('.confirm-dialog-button:has-text("تأیید")', force=True)  
                    break
                except Exception as last__e:
                    last_e = last__e
                    continue
            else: 
                return(f'[bright_cyan bold]Splus:[/bright_cyan bold]\n[bright_yellow]{last_e}[/bright_yellow]')


        #console.print('[bright_green]Extracting Data...[/bright_green]')

        #gender
        if page.locator('.icon.icon-splus-womanline').count() > 0: 
            gender = 'woman'
        elif page.locator('.icon.icon-splus-manline').count() > 0:
            gender = 'man'
        else: 
            gender = None
        #ispermium?
        if page.locator('.title .PremiumIcon[title="حساب پرو"]').count() > 0: 
            is_premium = True
        else: 
            is_premium = False

        #birthday
        try:
            class_birthday = page.locator('.icon.icon-calendar + .multiline-item')
            title_birthday = class_birthday.locator('.title').text_content(timeout=100)
            subtitle_birthday = class_birthday.locator('.subtitle').text_content(timeout=00)
            birthday = title_birthday + ', ' + subtitle_birthday
        except:
            birthday = None


        #id number
        try: 
            page_url = page.url
            id_number_match = re.search(r'#(\d+)', page_url)
            id_number = id_number_match.group(1)
        except: 
            id_number = None
            
        #name
        name = page.locator('.Profile .fullName').text_content(timeout=200)
        #last seen
        last_seen = page.locator('.user-status').nth(0).text_content(timeout=200)
        #username
        try:
            username = page.locator('.multiline-item:has(.subtitle:has-text("نام کاربری")) .title').nth(0).text_content(timeout=500)
            #username = username.removesuffix('نام کاربری')
        except:
            username = None
        #about me
        try:
            about_me = page.locator('.title.word-break.allow-selection').inner_text(timeout=100)
        except:
            about_me = None
        #profile
        try: 
            page.click('.ProfileInfo')
            try:
                page.wait_for_timeout(500)
                page.click('.ProfileInfo', timeout=1000)
            except:
                pass
            page.locator('.MediaViewerContent').first.wait_for(state='attached', timeout=5000)
            try: 
                profile_img = page.locator('.MediaViewerContent [style*="position: relative"] img').first
                page.wait_for_selector('.MediaViewerContent [style*="position: relative"] img', state='visible', timeout=5000)
                img_counter = 1
                profile_img.screenshot(path=f'./profile/{number_phone}/splus_{img_counter}.png')
                page.wait_for_timeout(1500)
                try:
                    next_btn = page.locator('.navigation.prev.false')
                    while next_btn.count() > 0 and next_btn.is_visible(): 
                        next_btn.click(force=True)
                        page.wait_for_timeout(500)
                        img_counter += 1
                        profile_img = profile_img = page.locator('.MediaViewerContent [style*="position: relative"] img').nth(1)
                        page.wait_for_selector('.MediaViewerContent [style*="position: relative"] img', state='visible', timeout=5000)
                        profile_img.screenshot(path=f'./profile/{number_phone}/splus_{img_counter}.png', omit_background=True)
                        page.wait_for_timeout(100)
                except:
                    console.print('[red]A Problem In Loeading Next Profile(0Splus), Pls Try Again.[/red]')
                    img_counter = None

            except:
                console.print('[red]A Problem In Loeading Profile(1Splus), Pls Try Again.[/red]')
                img_counter = None
        except:
            img_counter = 0    

        console.print('[cyan]Splus Finished Successfully![/cyan]')
            
        return(f'''
[bright_cyan bold]Splus:[/bright_cyan bold][bright_yellow]
[bold]Name:[/bold] {name}
[bold]UserName:[/bold] {username}
[bold]LastSeen:[/bold] {last_seen}
[bold]AboutMe:[/bold] {about_me}
[bold]Profiles:[/bold] {img_counter}
[bold]Gender:[/bold] {gender}
[bold]BirthDay:[/bold] {birthday}
[bold]IsPremium:[/bold] {is_premium} 
[bold]IdNumber:[/bold] {id_number} [/bright_yellow]''')
    
if __name__ == '__main__':
    number_phone = input('Enter Number Phone: ')
    while len(number_phone) != 10 or number_phone[0] != "9":
        number_phone = input('Enter Number Phone Again(Example: "91288899990"): ')
    result = get_data(number_phone)
    console.print(result)
