from playwright.sync_api import sync_playwright
from rich.console import Console
import sys
import os

console = Console()

def get_data(number_phone): 
    if not(os.path.exists('./browsers/shad_browser')): 
        return('[red]The shad_browser Folder Not Exists Please First Run "login.py"[/red]')
        sys.exit()
    
    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/shad_browser',
            headless=True,
            executable_path='/usr/bin/chromium',
            no_viewport=True,
            viewport={'width': 1720, 'height': 880}   
        )
    
        page = context.new_page()
        
        page.goto('https://my.shad.ir/messenger/')

        page.wait_for_timeout(2000)
        page.locator('.rbico.rbico-newchat_filled').wait_for(state='visible')
        page.click('.rbico.rbico-newchat_filled', force=True)
        page.wait_for_timeout(500) 
        page.locator('[rb-localize="new_message"]:has-text("پیام جدید")').click(force=True)
        page.click('.rbico-add.rp')
        page.wait_for_timeout(500)
        page.fill('[name="first_name"]', number_phone)
        page.wait_for_timeout(500)
        page.fill('[name="phone"]', number_phone)
        page.wait_for_timeout(500)
        page.click('.btn-primary:has-text("افزودن")')


        try: 
            page.locator('.popup-description:has-text("مخاطب حساب کاربری شاد ندارد.")').wait_for(state='attached', timeout=3000)
            return('\n[red]It Doesnt Have shad.[red]')
        except:
            pass

        page.locator('.popup.popup-create-contact.popup-new-media.active').wait_for(state='detached', timeout=20000)
        page.reload()
        page.wait_for_timeout(2000)
        page.locator('.rbico.rbico-newchat_filled').wait_for(state='visible')
        page.click('.rbico.rbico-newchat_filled', force=True)
        page.wait_for_timeout(500)
        page.locator('[rb-localize="new_message"]:has-text("پیام جدید")').click(force=True)    

        # for caution
        try: 
            page.wait_for_timeout(500)
            page.click(f'.user-title .peer-title:has-text("{number_phone}")', force=True, timeout=3000)
            page.wait_for_timeout(1000)
            page.click(f'.content .user-title .peer-title:has-text("{number_phone}")', force=True, timeout=3000)
        except: 

            while_counter = 0
            while while_counter < 5:
                try:
                    while_counter += 1
                    page.reload()
                    page.wait_for_timeout(2000)
                    page.locator('.rbico.rbico-newchat_filled').wait_for(state='visible')
                    page.click('.rbico.rbico-newchat_filled', force=True)
                    page.wait_for_timeout(500) 
                    page.locator('[rb-localize="new_message"]:has-text("پیام جدید")').click(force=True)
                    page.wait_for_timeout(500) 
                    page.click('.rbico-add.rp')
                    page.wait_for_timeout(500)
                    page.fill('[name="first_name"]', number_phone)
                    page.wait_for_timeout(500)
                    page.fill('[name="phone"]', number_phone)
                    page.wait_for_timeout(500)
                    page.click('.btn-primary:has-text("افزودن")')
                    page.locator('.popup.popup-create-contact.popup-new-media.active').wait_for(state='detached', timeout=20000)
                    page.reload()
                    page.wait_for_timeout(2000)
                    page.locator('.rbico.rbico-newchat_filled').wait_for(state='visible')
                    page.click('.rbico.rbico-newchat_filled', force=True)
                    page.wait_for_timeout(500)
                    page.locator('[rb-localize="new_message"]:has-text("پیام جدید")').click(force=True)

                    page.wait_for_timeout(500)
                    page.click(f'.user-title .peer-title:has-text("{number_phone}")', force=True, timeout=2000)
                    page.wait_for_timeout(1000)
                    page.click(f'.content .user-title .peer-title:has-text("{number_phone}")', force=True, timeout=2000)
                    break
                except Exception as last__e:
                    last_e = last__e
                    continue
            else: 
                return(f'[bright_green bold]Shad:[/bright_green bold]\n[bright_yellow]{last_e}[/bright_yellow]')


        page.wait_for_timeout(500)
        page.click('.btn-icon.rbico-edit.rp')
        page.click('[rb-localize="user_modal_delete_contact"]')
        page.click('[rb-localize="modal_ok"]')
        page.locator('.btn-icon.rbico-left.sidebar-close-button').nth(0).click(force=True)
        page.wait_for_timeout(500)

        page.click('.btn-icon.rbico-edit.rp')
        page.wait_for_timeout(500)
        page.locator('.btn-icon.rbico-left.sidebar-close-button').nth(0).click(force=True)
        page.wait_for_timeout(500)

        page.click('.btn-icon.rbico-edit.rp')
        page.wait_for_timeout(500)
        page.locator('.btn-icon.rbico-left.sidebar-close-button').nth(0).click(force=True)
        page.wait_for_timeout(500)

        page.click('.btn-icon.rbico-edit.rp')      

        #name
        name = page.locator('.profile-name').first.text_content()
        #last seen
        last_seen = page.locator('div.profile-subtitle').nth(1).text_content()
        #username
        try: 
            username = page.locator('.row-title.rbico.rbico-username').text_content(timeout=300)
        except:
            username = None
        #about me
        try: 
            about_me = page.locator('.row-title.rbico.rbico-info.pre-wrap').text_content(timeout=300)
            if not(about_me):
                about_me = None
        except:
            about_me = None
        
        page.wait_for_timeout(1000)
        page.locator('.btn-icon.rbico-left.sidebar-close-button').nth(0).click(force=True)

        #profile
        try:
            page.locator('.profile-avatars-avatar media-container').wait_for(state='visible', timeout=3000)
            page.click('.profile-avatars-avatar.media-container', timeout=500)
            try: 
                img_counter = 1
                profile_img = page.locator('.photo_modal_image').first
                page.wait_for_selector('.photo_modal_image', state='visible', timeout=5000)
                profile_date = page.locator('.media-viewer-date span').first.text_content().replace('/', '-')
                profile_img.screenshot(path=f'profile/{number_phone}/shad_{profile_date}-{img_counter}.png')
                page.wait_for_timeout(1000)

                try: 
                    next_btn = page.locator('.media-viewer-switcher.media-viewer-switcher-right')
                    while next_btn.count() > 0 and next_btn.is_visible(): 
                            next_btn.click(force=True)
                            page.wait_for_timeout(300)
                            img_counter += 1

                            profile_img = page.locator('.photo_modal_image').first
                            page.wait_for_selector('.photo_modal_image', state='visible', timeout=5000)
                            profile_date = page.locator('.media-viewer-date span').first.text_content().replace('/', '-')
                            profile_img.screenshot(path=f'profile/{number_phone}/shad_{profile_date}-{img_counter}.png')
                            page.wait_for_timeout(300)
                except:
                        console.print('[red]A Problem In Loeading Profile(0Shad), Pls Try Again.[/red]')
                        img_counter = None
            except:
                console.print('[red]A Problem In Loeading Profile(1Shad), Pls Try Again.[/red]')
                img_counter = None
        except:
            img_counter = 0             

        console.print('[bright_green]Shad Finished Successfully![/bright_green]')

        return(f'''
[bright_green bold]Shad:[/bright_green bold][bright_yellow]
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
