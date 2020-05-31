#!/usr/bin/python3

try:
   from os import system as cmd
   import requests as req
except:
     cmd('pip install requests')
     cmd('clear')

ua = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi3)'}

def iptoasn():
     ip = input('[?] ip: ')
     url2= 'https://api.bgpview.io/ip/'+ip
     res = req.get(url2,headers=ua).json()
     for i in res['data']['prefixes']:
         print()
         pfix = i['prefix']
         asn = i['asn']['asn']
         name = i['asn']['name']
         des = i['asn']['description']
         print('Prefix       :',pfix)
         print('Asn          : AS'+str(asn))
         print('Name         : '+name)
         print('Description  : '+des)
         print()
bnr = r'''

$$$$$$\ $$$$$$$\    $$\                $$$$$$\   $$$$$$\  $$\   $$\   
\_$$  _|$$  __$$\   $$ |              $$  __$$\ $$  __$$\ $$$\  $$ |   
  $$ |  $$ |  $$ |$$$$$$\    $$$$$$\  $$ /  $$ |$$ /  \__|$$$$\ $$ |   
  $$ |  $$$$$$$  |\_$$  _|  $$  __$$\ $$$$$$$$ |\$$$$$$\  $$ $$\$$ |
  $$ |  $$  ____/   $$ |    $$ /  $$ |$$  __$$ | \____$$\ $$ \$$$$ |
  $$ |  $$ |        $$ |$$\ $$ |  $$ |$$ |  $$ |$$\   $$ |$$ |\$$$ |
$$$$$$\ $$ |        \$$$$  |\$$$$$$  |$$ |  $$ |\$$$$$$  |$$ | \$$ |
\______|\__|         \____/  \______/ \__|  \__| \______/ \__|  \__|
                
          [?] Tools   : ip to asn  [?] Version : 1.0     
          [?] Coder   : bangtebe
                                                                 
'''


def main():
    cmd('clear')
    print(bnr)
    try:
        iptoasn()
    except:
      exit('\nexit')

