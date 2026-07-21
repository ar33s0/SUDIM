from playwright.sync_api import sync_playwright
from rich.console import Console 
import sys
import os

console = Console()

def get_data(number_phone): 

    if not(os.path.exists('browsers/eitaa_browser')): 
        return('[red]The eitaa_browser Folder Not Exists Please First Run "login.py"[/red]')
        sys.exit()

    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/eitaa_browser',
            headless=True,
            #executable_path='/usr/bin/chromium',
            no_viewport=True,
            viewport={'width': 1920, 'height': 1080}
        )

        page = context.new_page()
        page.goto('https://web.eitaa.com')

        #console.print('[bright_green]Adding...[/bright_green]')
        page.wait_for_timeout(500)
        page.click('.btn-icon.btn-menu-toggle.rp.sidebar-tools-button.is-visible')
        page.click('.btn-menu-item.tgico-user.rp')
        page.wait_for_timeout(500)
        page.click('.btn-circle.btn-corner.z-depth-1.tgico-add.rp.is-visible')
        page.fill('.input-field.input-field-phone .input-field-input', number_phone)
        page.locator('.name-fields .input-field-input').nth(0).fill(number_phone)
        page.wait_for_timeout(500)
        page.click('.btn-primary.btn-color-primary.rp', force=True)

        try: 
            page.locator('text="صاحب این شماره تلفن هنوز در ایتا ثبت نام نکرده است."').wait_for(state='attached', timeout=3000)
            return('\n[red]It Doesnt Have Eitaa.[red]')
        except:
            pass

        # for caution
        try: 
            page.wait_for_timeout(500)
            page.locator(f'.peer-title:has-text("{number_phone}")').nth(1).click(force=True)
            page.locator(f'.chat-info:has(.peer-title:has-text("{number_phone}"))').click(force=True)
        except: 
            while_counter = 0 
            while while_counter < 5: 
                try: 
                    while_counter += 1
                    page.reload()
                    page.click('.btn-icon.btn-menu-toggle.rp.sidebar-tools-button.is-visible')
                    page.click('.btn-menu-item.tgico-user.rp')
                    page.wait_for_timeout(500)
                    page.click('.btn-circle.btn-corner.z-depth-1.tgico-add.rp.is-visible')
                    page.fill('.input-field.input-field-phone .input-field-input', number_phone)
                    page.locator('.name-fields .input-field-input').nth(0).fill(number_phone)
                    page.wait_for_timeout(500)
                    page.click('.btn-primary.btn-color-primary.rp', force=True)            
                    page.wait_for_timeout(500)
                    page.locator(f'.chat-info:has(.peer-title:has-text("{number_phone}"))').click(force=True)
                    page.locator(f'.chat-info:has(.peer-title:has-text("{number_phone}"))').click(force=True)
                    break
                except Exception as last_e: 
                    continue
            else: 
                return(f'[orange1 bold]Eitaa:[/orange1 bold]\n[bright_yellow]{last_e}[/bright_yellow]') 

        page.click('.btn-icon.tgico-edit.rp')
        page.click('text="حذف مخاطب"')
        page.click('.btn.danger.rp:has-text("حذف")')
        page.locator('.btn-icon.tgico-left.sidebar-close-button').nth(1).click(force=True)
        page.wait_for_timeout(1000)

        #name
        name = page.locator('.profile-name').first.text_content()

        #id number
        try: 
            page_url = page.url
            id_number_match = re.search(r'#(\d+)', page_url)
            id_number = id_number_match.group(1)
        except: 
            id_number = None
        #last seen
        last_seen = page.locator('.profile-subtitle').text_content()
        #username
        try: 
            username = page.locator('.row-title.tgico.tgico-username').text_content(timeout=300)
            if len(username) == 1:
                username = None
        except:
            username = None
        #about me
        try: 
            about_me = page.locator('.row-title.tgico.tgico-info.pre-wrap').text_content(timeout=300)
            if len(about_me) == 1:
                about_me = None
        except:
            about_me = None
        

        #console.print('[bright_green]Extracting Profiles...[bright_green]')
        #profile
        try:
            page.click('.profile-avatars-avatar.media-container', timeout=500)
            try: 
                img_counter = 1
                profile_img = page.locator('.media-viewer-aspecter').first
                page.wait_for_selector('.media-viewer-aspecter', state='visible', timeout=5000)
                profile_date = page.locator('.media-viewer-date span').first.text_content().replace(' ', '-')
                profile_img.screenshot(path=f'profile/{number_phone}/eitaa_{profile_date}-{img_counter}.png')
                page.wait_for_timeout(1000)

                try: 
                    next_btn = page.locator('.media-viewer-switcher.media-viewer-switcher-right')
                    while next_btn.count() > 0 and next_btn.is_visible(): 
                            next_btn.click(force=True)
                            page.wait_for_timeout(500)
                            img_counter += 1

                            profile_img = page.locator('.media-viewer-aspecter').first
                            page.wait_for_selector('.media-viewer-aspecter', state='visible', timeout=5000)
                            profile_date = page.locator('.media-viewer-date span').first.text_content().replace(' ', '-')
                            profile_img.screenshot(path=f'profile/{number_phone}/eitaa_{profile_date}-{img_counter}.png')
                            page.wait_for_timeout(300)
                except:
                        console.print('[red]A Problem In Loeading Profile(0Eitaa), Pls Try Again.[/red]')
                        img_counter = None
            except:
                console.print('[red]A Problem In Loeading Profile(1Eitaa), Pls Try Again.[/red]')
                img_counter = None
        except:
            img_counter = 0             

        console.print('[orange1]Eitaa Finished Successfully![/orange1]')

        return(f'''
[orange1 bold]Eitaa:[/orange1 bold][bright_yellow]
[bold]Name:[/bold] {name}
[bold]UserName:[/bold] {username}
[bold]LastSeen:[/bold] {last_seen}
[bold]AboutMe:[/bold] {about_me}
[bold]Profiles:[/bold] {img_counter} 
[bold]IdNumber:[/bold] {id_number} [/bright_yellow]''')

if __name__ == '__main__':
    number_phone = input('Enter Number Phone: ')
    while len(number_phone) != 10 or number_phone[0] != "9":
        number_phone = input('Enter Number Phone Again(Example: "91288899990"): ')
    result = get_data(number_phone)
    console.print(result)

