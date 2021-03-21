from colorama import Fore, init, Style
import requests
import ctypes
import os

def Auth():
    IP = requests.get('http://api.ipify.org/').text
    r = requests.get('https://pastebin.com/raw/...............').text##Your raw link
    if IP in r:
        print('Matched !')
        pass
    else:
        os.system('cls')
        print(Fore.RED + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'IP address unauthorized!')
        print(Style.RESET_ALL + Fore.RED + ' -- ' + Fore.WHITE + Style.BRIGHT + 'Your IP: ' + IP)
        input()
        quit()

Auth()
## Your code here
