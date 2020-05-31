#!/usr/bin/python3

from os import system as cmd
import re
try:
   import requests as r
except:
     cmd('pip install requests')

try:
   from bs4 import BeautifulSoup as Bs
except:
      cmd('pip install bs4')

bnr = '''
 88  88  dP"Yb  .dP"Y8 888888  dP"Yb  88 88""Yb
 88  88 dP   Yb `Ybo."   88   dP   Yb 88 88__dP
 888888 Yb   dP o.`Y8b   88   Yb   dP 88 88"""
 88  88  YbodP  8bodP'   88    YbodP  88 88  v1.0
'''

def v1(do):
    dt ={"hostname":do,"submit":{"submit":"Check Hostname"}}
    res = r.post(url='https://sshocean.com/hostname-to-ip',data=dt,headers={'User-Agent':'bang tebe'})
    p = Bs(res.text,'html.parser')
    f = p.find('div',class_="alert alert-success")
    print(f.text)



def v2(hos):
   dt = {'DOMAINNAME':hos,"Lookup IP Address":"Lookup IP Address"}
   res = r.post(url='https://whatismyipaddress.com/hostname-ip',data=dt).text
   bs = Bs(res,'html.parser')
   for p in bs.findAll('div',id="section_left_3rd"):
       for s in p.findAll('p'):
           if 'Hostname:' in str(s):
               s = str(s)
               f = re.findall(r'(.*)',s)
               '''
               hn = re.findall(r'Lookup Hostname: (.*?)<br/>',f[2].strip())
               print('Hostname  :',hn[0])'''
               print('Ip result : ')
               for ip in f[4].strip().split('<br/>'):
                   ips = re.findall(r'Lookup IPv4 Address: <a href="/ip/(.*?)">',ip)
                   if len(ips) == 1:
                      print('           ',ips[0])
               print()



def main():
   cmd('clear')
   print(bnr)
   hos = input('Hostname  : ')
   h = hos.split(' ')
   if ' v1' in hos:
      v1(h[0])
   elif ' v2' in hos:
        v2(h[0])
   else:
       v1(h[0])
