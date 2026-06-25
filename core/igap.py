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

        editer_number_phone = '+98' + number_phone

        page = context.new_page()
        
        page.goto('https://web.igap.net/')

        page.click('.icon-ig-contacts-outline')
        page.click('.icon-contacts')
        page.click('.icon-add-member')

        page.fill('[name="firstName"]', number_phone)
        page.fill('input#outlined-controlled', editer_number_phone)

        page.locator('#portals header button').first.click()
        page.locator('#portals header button').first.click()

        try: 
            page.locator('.icon-error').wait_for(state='visible', timeout=1000)
            return('[red]Its Doesnt Have igap.[/red]')
        except: 
            pass

        page.locator(f'.flex.flex-row.justify-between').filter(has_text=number_phone).first.click()
        page.locator('.font-bold.flex.flex-row.label-md.text-surface-on.gap-sm.items-center').filter(has_text=number_phone).click()

        page.locator('.h-[90%] .icon-ig-kebab-menu-outline')

        page.wait_for_timeout(100000)


if __name__ == '__main__':
    number_phone = '9120004444' #input('Enter Number Phone: ')
    #while len(number_phone) != 10 or number_phone[0] != "9":
        #number_phone = input('Enter Number Phone Again(Example: "91288899990"): ')
    result = get_data(number_phone)
    console.print(result)
