#!/usr/bin/python3

##---- MODULE
try:
   from os import system as cmd;from time import sleep
   import requests as req
except:
     cmd('pip install requests')
     cmd('clear')


sr = []


##---- PP
def check(ip,t):
   try:
      res = req.get(url=ip.strip('\n'[0]),timeout=t,allow_redirects=False)
      o = '[  OPEN  ] '+ip
      g = '           GET '+res.url
      s = str(res.status_code)
      sr.append(res.reason)
      st = '           HTTP/ '+s+' '+sr[0]
      print(o+'\n'+'\n'+g)
      print(st)
      with open('out_.txt','a') as wr:
           wr.write('\n'+o+'\n'+'\n'+g+'\n'+st+'\n')
      for hed in res.headers:
          hd = '           '+str(hed+': '+res.headers[hed])
          print(hd)
          with open('out_.txt','a') as w:
               w.write(hd+'\n')
      sr.clear()
      print()
   except KeyboardInterrupt:
         print('exit')
         exit()
   except Exception as err:
         print('[ CLOSED ] '+ip.strip('\n'))


def scan(web,ip,t):
    try:
       res = req.get(url=web,proxies={'http':'http://'+ip},timeout=t,allow_redirects=False)
       o = '[  OPEN  ] '+web+' - '+ip.strip('\n')
       g = '           GET '+res.url+' - '+ip.strip('\n')
       s = str(res.status_code)
       sr.append(res.reason)
       st = '           HTTP/ '+s+' '+sr[0]
       rst = o+'\n'+'\n'+g+'\n'+st
       print(rst)
       with open('out_.txt','a') as wr:
           wr.write('\n'+rst)
       for hed in res.headers:
           hd = '           '+str(hed+': '+res.headers[hed])
           print(hd)
           with open('out_.txt','a') as w:
                w.write(hd+'\n')
       sr.clear()
       print()
    except KeyboardInterrupt:
          print('exit')
          exit()
    except Exception as err:
         print('[ CLOSED ] '+web.strip('\n')+' - '+ip.strip('\n'))

def mm(do,ti):
   if '.' in ti:
      if 'http://' in do or 'https://' in do:
         check(ip=do,t=float(ti))
      else:
          check(ip='http://'+do,t=float(ti))
   else:
       if 'http://' in do or 'https://' in do:
           check(ip=do,t=int(ti))
       else:
           check(ip='http://'+do,t=int(ti))


def m(do,pr,ti):
   if '.' in ti:
      if 'http://' in do or 'https://' in do:
         scan(web=do,ip=pr,t=float(ti))
      else:
          scan(web='http://'+do,ip=pr,t=float(ti))
   else:
       if 'http://' in do or 'https://' in do:
           scan(web=do,ip=pr,t=int(ti))
       else:
           scan(web='http://'+do,ip=pr,t=int(ti))


## ------ BANNER
b =r'''

  $$\   $$\ $$$$$$$\            $$\                           $$\       
  $$ |  $$ |$$  __$$\           $$ |                          $$ |      
  $$ |  $$ |$$ |  $$ | $$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\ 
  $$$$$$$$ |$$$$$$$  |$$  _____|$$  __$$\ $$  __$$\ $$  _____|$$ | $$  |
  $$  __$$ |$$  ____/ $$ /      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  / 
  $$ |  $$ |$$ |      $$ |      $$ |  $$ |$$   ____|$$ |      $$  _$$<  
  $$ |  $$ |$$ |      \$$$$$$$\ $$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ 
  \__|  \__|\__|       \_______|\__|  \__| \_______| \_______|\__|  \__|
                                                                                                                                                                                                                         
       [!] Tools   : Host/Proxy Checker     listcheck:
       [!] Coder   : bangtebe                    [?] 1. Direct/Non
       [!] Version :  1.0                        [?] 2. Multi Mode
      
'''

b2 ='''

     list:
          [?] 1. url
          [?] 2. Proxy
'''

b3 ='''

     list:
          [?] 1. Direct
          [?] 2. Multi Direct
          [?] 3. Non Direct
'''

##---- MAIN
def main1():
   c = input('[!] choice: ')
   if c == '1':
      cmd('clear')
      print(b3)
      ccc = input('[!] choice: ')
      if ccc == '1':
         do = input('[?] url/proxy: ')
         ti = input('[?] Timeout: ' )
         mm(do=do,ti=ti)

      elif ccc == '3':
           do = input('[?] url: ')
           pr = input('[?] usr:pss@proxy:port > ')
           ti = input('[?] Timeout: ' )
           m(do=do,pr=pr,ti=ti)
      elif ccc == '2':
           try:
              do = input('[?] Dir url/proxy: ')
              pot = input('[?] Port    : ')
              ti = input('[?] Timeout : ' )
              for i in open(do).readlines():
                  if len(i) > 3:
                     ip_split = i.split(':')
                     if len(ip_split) == 1:
                        if len(pot) > 0:
                           res_ip = i.strip('\n'[0])+':'+pot
                           mm(do=res_ip,ti=ti)

                        else:mm(do=i.strip('\n'[0]),ti=ti)

                     else:mm(do=i.strip('\n'[0]),ti=ti)

           except FileNotFoundError:
                  print('file',do,'tidak di temukan!')
   elif c == '2':
        cmd('clear')
        print(b2)
        cc = input('[!] choice: ')
        if cc == '1':
           try:
              do = input('[?] Dir url: ')
              pr = input('[?] usr:pss@proxy:port > ')
              ti = input('[?] Timeout: ' )
              for p in open(do).readlines():
                  if len(p) > 5:
                     m(do=p.strip('\n'[0]),pr=pr,ti=ti)
           except FileNotFoundError:
                 print(do,'tidak di temukan!')

        elif cc == '2':
              try:
                 do = input('[?] url: ')
                 pr = input('[?] Dir usr:pss@proxy:port > ')
                 ti = input('[?] Timeout: ' )
                 for p in open(pr).readlines():
                     if len(p) > 5:
                        m(do=do,pr=p.strip('\n'[0]),ti=ti)
              except FileNotFoundError:
                     print(pr,'tidak di temukan!')
        else:
              exit('\nexit')
   else:exit('\nexit')

def main():
  try:
     cmd('clear')
     print(b)
     main1()
  except:
    exit('\nexit')

