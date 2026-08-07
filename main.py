from rich.console import Console
from time import sleep
import sys
#import concurrent.futures
from core import bale, rubika, eitaa, splus, shad, igap
import re
import os

proxy_off = True
if proxy_off == True: 
    proxy_vars = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']
    for var in proxy_vars: 
        os.environ.pop(var, None)


console = Console()

console.print("""[cyan][bold]
  ███████╗ ██╗   ██╗ ██████╗  ██╗ ███╗   ███╗
  ██╔════╝ ██║   ██║ ██╔══██╗ ██║ ████╗ ████║
  ███████╗ ██║   ██║ ██║  ██║ ██║ ██╔████╔██║
  ╚════██║ ██║   ██║ ██║  ██║ ██║ ██║╚██╔╝██║
  ███████║ ╚██████╔╝ ██████╔╝ ██║ ██║ ╚═╝ ██║
  ╚══════╝  ╚═════╝  ╚═════╝  ╚═╝ ╚═╝     ╚═╝
   -Scrap User Data From Iranian Messengers-
                  
https://github.com/ar33s0 | -By Ares[/bold]
[/cyan]""")

if len(sys.argv) > 1:
    while len(sys.argv[1]) != 10 or sys.argv[1][0] != "9":
        number_phone = input('Enter Number Phone Again(Example: "91288899990"): ')
    number_phone = sys.argv[1]

else: 
    number_phone = input('Enter Number Phone: ')
    while len(number_phone) != 10 or number_phone[0] != "9":
        number_phone = input('Enter Number Phone Again(Example: "91288899990"): ')

#so i dont have a good internet ):
#with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #future_bale = executor.submit(bale, number_phone)
    #future_rubika = executor.submit(rubika, number_phone)
    #future_splus = executor.submit(splus, number_phone)
    #future_eitaa = executor.submit(eitaa, number_phone)
    #future_eitaa = executor.submit(shad, number_phone)
    #console.print(
        #future_bale.result(),
        #print('='*24),
        #future_rubika.result(),
        #print('='*24),
        #future_splus.result(),
        #print('='*24),
        #future_eitaa.result(),
        #print('='*24),
        #future_shad.result()

iran_mobile_prefixes = {    
    "910": "MCI (همراه اول) - دائمی/اعتباری",
    "911": "MCI (همراه اول) - دائمی/اعتباری",
    "912": "MCI (همراه اول) - عمدتاً دائمی",
    "913": "MCI (همراه اول) - دائمی/اعتباری",
    "914": "MCI (همراه اول) - دائمی/اعتباری",
    "915": "MCI (همراه اول) - دائمی/اعتباری",
    "916": "MCI (همراه اول) - دائمی/اعتباری",
    "917": "MCI (همراه اول) - دائمی/اعتباری",
    "918": "MCI (همراه اول) - دائمی/اعتباری",
    "919": "MCI (همراه اول) - اعتباری",
    "990": "MCI (همراه اول) - اعتباری",
    "991": "MCI (همراه اول) - دائمی/اعتباری",
    "992": "MCI (همراه اول) - اعتباری",
    "993": "MCI (همراه اول) - اعتباری",
    "994": "MCI (همراه اول) - اعتباری (انارستان/نوجوانان)",
    "996": "MCI (همراه اول) - اعتباری",

    "930": "Irancell (ایرانسل) - اعتباری/دائمی",
    "933": "Irancell (ایرانسل) - اعتباری/دائمی",
    "934": "TKC (کیش) / Irancell (ایرانسل) - اعتباری/دائمی",
    "935": "Irancell (ایرانسل) - اعتباری/دائمی",
    "936": "Irancell (ایرانسل) - اعتباری/دائمی",
    "937": "Irancell (ایرانسل) - اعتباری/دائمی",
    "938": "Irancell (ایرانسل) - اعتباری/دائمی",
    "939": "Irancell (ایرانسل) - اعتباری/دائمی",
    "901": "Irancell (ایرانسل) - اعتباری/دائمی",
    "902": "Irancell (ایرانسل) - دائمی/اعتباری",
    "903": "Irancell (ایرانسل) - اعتباری/دائمی",
    "904": "Irancell (ایرانسل) - اعتباری (سیم‌کارت کودک)",
    "905": "Irancell (ایرانسل) - اعتباری/دائمی",
    "906": "Irancell (ایرانسل) - اعتباری/دائمی",

    "920": "Rightel (رایتل) - دائمی",
    "921": "Rightel (رایتل) - اعتباری",
    "922": "Rightel (رایتل) - اعتباری",
    "923": "Rightel (رایتل) - اعتباری",

    "932": "Taliya (تالیا) - اعتباری",
    "998": "Shatel Mobile (شاتل موبایل) - اعتباری/دائمی",
    "999": "Samantel (سامانتل) - دائمی/اعتباری"
}

if number_phone[:3] in iran_mobile_prefixes: 
    console.print(f'[bright_yellow]\n{iran_mobile_prefixes[number_phone[:3]]}\n[/bright_yellow]')

funcs = {
    'eitaa_result': eitaa,
    'bale_result': bale,
    'splus_result': splus,
    'rubika_result': rubika,
    'shad_result': shad,
    'igap_result': igap
}

results = {}

for name, func in funcs.items(): 
    try:
        results[name] = func(number_phone)
        sleep(0.5)
    except Exception as e: 
        results[name] = f'{name}: \n {e}'

for name, result in results.items(): 
    console.print(result)
    print('='*24)
