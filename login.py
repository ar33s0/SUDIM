from playwright.sync_api import sync_playwright
from rich.console import Console
import os

console = Console()

#bale
if not(os.path.exists('browsers/bale_browser')): 
    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/bale_browser',
            headless=False,
            executable_path='/usr/bin/chromium',
            no_viewport=True
        )    
        page = context.new_page()
        page.goto('https://web.bale.ai')
        console.print('[dark_green]Please Login[/dark_green]')
        input('If You Login Enter To Next: ')
        console.print('[dark_green]Bale is Done![/dark_green]')
else: 
    console.print('[dark_green]The Browser Bale Folder Already Exist. If There Is Have A Problem Delete "bale_browser" And Run This Code Again.[/dark_green]')

#rubika
if not(os.path.exists('browsers/rubika_browser')): 
    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/rubika_browser',
            headless=False,
            executable_path='/usr/bin/chromium',
            no_viewport=True
        )    
        page = context.new_page()
        page.goto('https://web.rubika.ir')
        console.print('\n[red]Please Login[/red]')
        input('If You Login Enter To Next: ')
        console.print('[red]Rubika is Done![red]')
else: 
    console.print('[red]The Browser Rubika Folder Already Exist. If There Is Have A Problem Delete "rubika_browser" And Run This Code Again.[red]')
#splus
if not(os.path.exists('browsers/splus_browser')): 
    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/splus_browser',
            headless=False,
            executable_path='/usr/bin/chromium',
            no_viewport=True
        )    
        page = context.new_page()
        page.goto('https://web.splus.ir')
        console.print('\n[cyan]Please Login[/cyan]')
        input('If You Login Enter To Next: ')
        console.print('[cyan]Splus is Done![/cyan]')
else:
    console.print('[bright_cyan]The Browser Splus Folder Already Exist. If There Is Have A Problem Delete "splus_browser" And Run This Code Again.[/bright_cyan]')

#eitaa
if not(os.path.exists('browsers/eitaa_browser')): 
    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/eitaa_browser',
            headless=False,
            executable_path='/usr/bin/chromium',
            no_viewport=True
        )    
        page = context.new_page()
        page.goto('https://web.eitaa.com')
        console.print('\n[orange1]Please Login[/orange1]')
        input('If You Login Enter To Next: ')
        console.print('[orange1]Eitaa is Done![/orange1]')
else: 
    console.print('[orange1]The Browser Eitaa Folder Already Exist. If There Is Have A Problem Delete "eitaa_browser" And Run This Code Again.[/orange1]')

#shad
if not(os.path.exists('browsers/shad_browser')): 
    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/shad_browser',
            headless=False,
            executable_path='/usr/bin/chromium',
            no_viewport=True
        )    
        page = context.new_page()
        page.goto('https://my.shad.ir')
        console.print('\n[bright_green]Please Login[/bright_green]')
        input('If You Login Enter To Next: ')
        console.print('[bright_green]shad is Done![/bright_green]')
else: 
    console.print('[bright_green]The Browser Shad Folder Already Exist. If There Is Have A Problem Delete "shad_browser" And Run This Code Again.[/bright_green]')

#igap
if not(os.path.exists('browsers/igap_browser')): 
    with sync_playwright() as p: 
        context = p.chromium.launch_persistent_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
            user_data_dir='./browsers/igap_browser',
            headless=False,
            executable_path='/usr/bin/chromium',
            no_viewport=True
        )    
        page = context.new_page()
        page.goto('https://web.igap.net')
        console.print('\n[lime]Please Login[/lime]')
        input('If You Login Enter To Next: ')
        console.print('[lime]Igap is Done![/lime]')
else: 
    console.print('[lime]The Browser Igap Folder Already Exist. If There Is Have A Problem Delete "igap_browser" And Run This Code Again.[/lime]')