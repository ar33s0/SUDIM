from playwright.sync_api import sync_playwright
from rich.console import Console 
import os

console = Console()

def get_data(number_phone): 

    if not(os.path.exists('browsers/igap_browser')): 
        return('[red]The igap_browser Folder Not Exists Please First Run "login.py"[/red]')

    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/igap_browser',
            headless=False,
            #executable_path='/usr/bin/chromium',
            no_viewport=True,
            viewport={'width': 1920, 'height': 1080}
        )

        edited_number_phone = '+98' + number_phone

        page = context.new_page()
        
        page.goto('https://web.igap.net/')

        page.click('.icon-ig-contacts-outline')
        page.click('.icon-contacts')
        page.click('.icon-add-member')

        page.fill('[name="firstName"]', number_phone)
        page.fill('input#outlined-controlled', edited_number_phone)

        page.locator('#portals header button').first.click()
        page.locator('#portals header button').first.click()

        try: 
            page.locator('.icon-error').wait_for(state='visible', timeout=2000)
            return('[red]Its Doesnt Have igap.[/red]')
        except: 
            pass

        try: 
            page.locator(f'.flex.flex-row.justify-between').filter(has_text=number_phone).wait_for(state='visible', timeout=3000)
            page.locator(f'.flex.flex-row.justify-between').filter(has_text=number_phone).first.click()
            page.locator('.font-bold.flex.flex-row.label-md.text-surface-on.gap-sm.items-center').filter(has_text=number_phone).click()
        except: 
            while_counter = 0
            while while_counter < 3: 
                try: 
                    page.reload()
                    page.click('.icon-ig-contacts-outline')
                    page.click('.icon-contacts')
                    page.click('.icon-add-member')

                    page.fill('[name="firstName"]', number_phone)
                    page.fill('input#outlined-controlled', edited_number_phone)

                    page.locator('#portals header button').first.click()
                    page.locator('#portals header button').first.click()
                    page.locator(f'.flex.flex-row.justify-between').filter(has_text=number_phone).first.click()
                    page.locator('.font-bold.flex.flex-row.label-md.text-surface-on.gap-sm.items-center').filter(has_text=number_phone).click()
                except Exception as last_e: 
                    page.wait_for_timeout(1000)
                    last_e = last_e
                    continue
            else: 
                return('[bright_green bold]igap:[/bright_green bold]\n[bright_yellow]{last_e}[/bright_yellow]')



        page.locator('.h-[90%] .icon-ig-kebab-menu-outline')

        page.locator('.flex.flex-row.justify-between', has_text=number_phone).locator('.icon-ig-kebab-menu-outline.text-2xl').first.click()
        page.locator('.icon-delete.text-surface-on_variant.text-xl.mx-1').first.locator('..').click()
        page.click('#next-button')

        page.locator('.flex.flex-row.justify-between').filter(has_text=number_phone).wait_for(state='detached', timeout=4000)
        page.wait_for_timeout(2000)

        #name
        while_counter2 = 0
        while while_counter2 < 3: 
            name = page.locator('.absolute.bg-surface-bright.text-surface-on.px-8.py-1.rounded-lg.text-xl.font-semibold').text_content(timeout=500)
            if name != edited_number_phone: 
                break
            page.wait_for_timeout(1000)
            while_counter2 += 1

        #last_seen
        last_seen = page.locator('.flex.flex-col.mx-2.truncate .text-xs').text_content(timeout=500)

        #username
        try: 
            username = page.locator('.text-entity-link').text_content(timeout=500)
        except: 
            username = None

        #about_me
        try: 
            about_me = page.locator('.pr-2.font-medium.text-content.transition.ease-in-out.duration-300').nth(1).text_content(timeout=500)
        except: 
            about_me = None

        #profile
        img_counter = 0
        try: 
            page.locator('.relative.select-none.text-white').wait_for(state='attached', timeout=2000)
            page.click('.relative.select-none.text-white')
            page.locator('.cursor-pointer.w-full.transition.mt-3').nth(0).wait_for(state='visible', timeout=500)
            try: 
                profiles_item = page.locator('.cursor-pointer.w-full.transition.mt-3')
                next_button = page.locator('.swiper-button-next')
                for img_counter in range(profiles_item.count()): 
                    try: 
                        try: 
                            profiles_item.nth(img_counter).wait_for(state='visible', timeout=4000)
                        except:
                            console.print(f'[red]A Problem In Loading Profile {img_counter+1} In Igap.[/red]')
                        profiles_item.nth(img_counter).screenshot(path=f'profile/{number_phone}/igap-{img_counter+1}.png')
                        page.wait_for_timeout(1000)
                        if img_counter + 1 != profiles_item.count(): 
                            next_button.nth(img_counter).click(force=True)
                    except Exception as e2: 
                        console.print(f'[red]A Problem In Loading Profile(0Igap), Pls Try Again.[/red]')
                        continue
            except Exception as e: 
                console.print(f'[red]A Problem In Loading Profile(1Igap), Pls Try Again.[/red]')
        except: 
            img_counter = None

        console.print('[bright_green]Igap Finished Successfully![/bright_green]')

        return(f'''
[bright_green bold]Igap:[/bright_green bold][bright_yellow]
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
