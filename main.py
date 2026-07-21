from rich.console import Console
from time import sleep
import sys
#import concurrent.futures
from core import bale, rubika, eitaa, splus, shad
import json

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

funcs = {
    'eitaa_result': eitaa,
    'bale_result': bale,
    'splus_result': splus,
    'rubika_result': rubika,
    'shad_result': shad
}

results = {}

for name, func in funcs.items(): 
    try:
        results[name] = func(number_phone)
        sleep(1.5)
    except Exception as e: 
        results[name] = f'{name}: \n {e}'

with open(f'profile/{number_phone}/data.json', 'w', encoding='utf-8') as file: 
    json.dump(results, file, indent=4, ensure_ascii=False)

for name, result in results.items(): 
    console.print(result)
    print('='*24)

console.print(f'[Blue]Data and profiles saved to profile/{number_phone}[/blue]')
