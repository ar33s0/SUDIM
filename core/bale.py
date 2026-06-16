from playwright.sync_api import sync_playwright
from rich.console import Console 
import sys
import os

console = Console()

def get_data(number_phone): 
    if not(os.path.exists('browsers/bale_browser')): 
        console.print('[red]The bale_browser Folder Not Exists Please First Run "login.py"[/red]')
        sys.exit()

    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/bale_browser',
            headless=True,
            #executable_path='/usr/bin/chromium',
            viewport={'width': 1920, 'height': 1080}
        )    
        
        page = context.new_page()
        page.goto('https://web.bale.ai')

        page.locator('#main_navigation_wrapper').wait_for(state='visible', timeout=10000)

        #for caution
        try: 
            page.click('[aria-label="بستن"]', timeout=500)
        except: 
            pass


        #console.print('[bright_green]Adding...[/bright_green]')
        page.click('text=مخاطبین')
        page.click('text=افزودن مخاطب')
        page.fill('input[aria-label="شماره همراه"]', number_phone )
        page.wait_for_timeout(500)
        page.fill('input[aria-label="نام"]', number_phone )
        page.wait_for_timeout(1000)
        page.click('[aria-label="افزودن"]')

        try: 
            page.locator('text="مخاطب مورد نظر در «بله» حساب کاربری ندارد."').wait_for(state='attached', timeout=3000)
            return('\n[red]It Doesnt Have Bale.[red]')
        except:
            pass

        # for caution
        while_counter = 0

        try:
            page.reload()
            page.click(f'text={number_phone}', force=True)
        except : 
            while while_counter < 5: 
                try: 
                    while_counter += 1                
                    page.reload()
                    page.click('text=افزودن مخاطب')
                    page.fill('input[aria-label="شماره همراه"]', number_phone )
                    page.wait_for_timeout(500)
                    page.fill('input[aria-label="نام"]', number_phone )
                    page.wait_for_timeout(1000)
                    page.click('[aria-label="افزودن"]')
                    page.reload()
                    page.click(f'text={number_phone}', force=True)
                    break
                except Exception as last_e:
                    continue
            else: 
                return(f'[dark_green bold]Bale:[/dark_green bold]\n[bright_yellow]{last_e}[/bright_yellow]')

        page.click('[aria-label="ChatAppBar"]')
        page.wait_for_timeout(500)

        page.locator('[data-testid="menu-icon"]').nth(1).click(force=True)
        page.wait_for_timeout(500)
        page.click('text=حذف مخاطب')
        page.wait_for_timeout(500)
        page.click('[aria-label="حذف مخاطب"]')

        page.wait_for_timeout(500)

        #console.print('[bright_green]Extracting Data...[/bright_green]')

        #username
        try:
            username = page.locator('[data-testid="username"] span').text_content(timeout=300)
        except: 
            username = None
        #about me
        try: 
            about_me = ''
            elements_about_me = page.locator('[data-testid="about"] span').all()
            for element in elements_about_me: 
                about_me += element.text_content()
            if not(about_me): 
                about_me = None
        except: 
            about_me = None

        #name
        name = page.locator('.kSqtzD').text_content()
        #last seen
        last_seen = page.locator('.BHJZrd').text_content()

        #console.print('[bright_green]Extracting Profiles...[bright_green]')
        #profile
        try: 
            page.locator('[data-sentry-component="SharedMediaTabContentView"] [aria-label="avatar"]').click(force=True)
            page.wait_for_timeout(500)
            page.locator('.swiper-slide-active').first.wait_for(state='attached', timeout=1000)
            try:
                profile_img = page.locator('.swiper-slide-active img').first
                img_counter = 1
                page.wait_for_selector('.swiper-slide-active img', state='visible', timeout=5000)
                profile_img.screenshot(path=f'profile/{number_phone}/bale_{img_counter}.png')

                next_btn = page.locator('.swiper-button-next')
                try: 
                    while next_btn.count() > 0 and next_btn.is_visible(): 
                        next_btn.click(force=True)
                        page.wait_for_timeout(500)
                        img_counter += 1

                        profile_img = profile_img = page.locator('.swiper-slide-active img').first
                        page.wait_for_selector('.swiper-slide-active img', state='visible', timeout=5000)
                        profile_img.screenshot(path=f'profile/{number_phone}/bale_{img_counter}.png')
                        page.wait_for_timeout(500)
                except: 
                    console.print('[red]A Problem In Loeading Profile(0Bale), Pls Try Again.[/red]')
                    img_counter = None

            except: 
                console.print('[red]A Problem In Loeading Profile(1Bale), Pls Try Again.[/red]')
                img_counter = None
        except: 
            img_counter = 0

        console.print('[dark_green]Bale Finished Successfully![/dark_green]')
        
        return(f'''
[dark_green bold]Bale:[/dark_green bold][bright_yellow]
[bold]Name:[/bold] {name}
[bold]UserName:[/bold] {username}
[bold]LastSeen:[/bold] {last_seen}
[bold]AboutMe:[/bold] {about_me}
[bold]Profiles:[/bold] {img_counter} [/bright_yellow]''')

if __name__ == '__main__':
    number_phone = input('Enter Number Phone: ')
    while len(number_phone) != 10 or number_phone[0] != "9":
        number_phone = input('Enter Number Phone Again(Example: "91288899990"): ')
    result = get_data(number_phone)
    console.print(result)
