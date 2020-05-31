#!user/bin/python3

import os
try:
    from time import sleep
    import requests as r
except:
    os.system('pip install requests')


r200 = []
# mport = []
rspon = []

class Proxy():
    def __init__(self):
       self.Mode()

    def Hasil(self):
        rs = len(r200)
        if rs > 0:
           print(f'keberuntungan anda sebanyak: {rs} proxy')
           try:
              saved = input('example: /sdcard/r.txt\n[?] save as: ')
              for i in r200:
                with open(saved,'a') as w:
                    w.write(i+'\n')
              print('Done!')
           except:
                print('\nfailed')
        else: print('anda tidak beruntung kali ini ×_×\n')

    def no_respon(self,r_url,rangeproxy,port,bughost,timot,n):
        if len(bughost) == 0:
           try:
              res = r.get(r_url,timeout=int(timot),allow_redirects=False)
              print(f'Line           : {n}')
              print('Status         : OPEN')
              print(f'Proxy & Port   : {rangeproxy}:{port}')
              print(f'Status Code    : {res.status_code} {str(res.reason)}\n')
              r200.append(f'{rangeproxy}:{port} Response: {res.status_code} {res.reason}')
           except Exception as err:
               # exit(err)
               print(f'Line           : {n}')
               print('Status         : CLOSED')
               print(f'Proxy & Port   : {rangeproxy}:{port}\n')
           except KeyboardInterrupt:
               self.Hasil()
               exit('exit code')
        else:
           try:
              res = r.get(url=bughost,proxies={'http':r_url},timeout=int(timot),allow_redirects=False)
              print(f'Line           : {n}')
              print('Status         : OPEN')
              print(f"Proxy & Port   : {rangeproxy}:{port} - {bughost}")
              print(f'Status Code    : {res.status_code} {str(res.reason)}\n')
              r200.append(f'{rangeproxy}:{port} - {bughost} Response: {res.status_code} {res.reason}')
           except Exception as err:
               print(f'Line           : {n}')
               print('Status         : CLOSED')
               print(f"Proxy & Port   : {rangeproxy}:{port} - {bughost}\n")
           except KeyboardInterrupt:
               self.Hasil()
               exit('exit code')

    def w_respon(self,r_url,rangeproxy,port,bughost,timot,n):
        if len(bughost) == 0:
            try:
                res = r.get(r_url,timeout=int(timot),allow_redirects=False)
                print(f'Line           : {n}')
                print('Status         : OPEN')
                print(f'Proxy & Port   : {rangeproxy}:{port}')
                print(f'Status Code    : {res.status_code} {str(res.reason)}')
                r200.append(f'{rangeproxy}:{port} Response: {res.status_code} {res.reason}')
                print()
                rg = '                GET '+res.url
                reas = ['                HTTP/ '+str(res.status_code)+' '+str(res.reason)]
                rs = '\n'+rg+'\n'+reas[0]
                print(rs)
                with open('rspon_no_host.txt','a') as w:
                     w.write('\n'+rs+'\n')
                for hed in res.headers:
                    h = [hed+': '+res.headers[hed]]
                    resp = '                '+h[0]
                    print(resp)
                    rspon.append(resp)
                    # print('               ',hed+': '+res.headers[hed])
                for wr in rspon:
                    with open('rspon_no_host.txt','a') as w:
                        w.write(wr+'\n')
                rspon.clear()
                print('\n')
            except Exception as err:
                print(f'Line           : {n}')
                print('Status         : CLOSED')
                print(f'Proxy & Port   : {rangeproxy}:{port}\n')
            except KeyboardInterrupt:
                self.Hasil()
                exit('exit code')
        else:
            try:
                res = r.get(url=bughost,proxies={'http':r_url},timeout=int(timot),allow_redirects=False)
                print(f'Line           : {n}')
                print('Status         : OPEN')
                print(f"Proxy & Port   : {rangeproxy}:{port} - {bughost}")
                print(f'Status Code    : {res.status_code} {str(res.reason)}\n')
                r200.append(f'{rangeproxy}:{port} - http://{bughost} Response: {res.status_code} {res.reason}')
                rg = '                GET '+bughost+' - '+rangeproxy+':'+port
                reas = ['                HTTP/ '+str(res.status_code)+' '+str(res.reason)]
                rs = '\n'+rg+'\n'+reas[0]
                print(rs)
                with open('rspon_with_host.txt','a') as w:
                     w.write('\n'+rs+'\n')
                for hed in res.headers:
                    h = [hed+': '+res.headers[hed]]
                    resp = '                '+h[0]
                    print(resp)
                    rspon.append(resp)
                    # print('               ',hed+': '+res.headers[hed])
                for wr in rspon:
                    with open('rspon_with_host.txt','a') as w:
                        w.write(wr+'\n')
                rspon.clear()
                print('\n')
            except Exception as err:
                print(f'Line           : {n}')
                print('Status         : CLOSED')
                print(f"Proxy & Port   : {rangeproxy}:{port} - {bughost}\n")
            except KeyboardInterrupt:
                self.Hasil()
                exit('exit code')

    def Mode(self):
        try:
            choose = input(mod+'[?] choose    : ')
            if choose == '1':
                cok = input('[?] from (d)ir or (t)empel : ')
                if 't' == cok:
                  input_1 = input('[?] range     : ')
                  port = input(   '[?] port      : ')
                  bughost = input('[?] host      : ')
                  timot = input(  '[?] timeout   : ')
                  mport = port.split(',')
                  n = 0
                  print('CHECKING......')
                  for port in mport:
                      for rr in range(0,255):
                          n +=1
                          a = input_1.split('/')
                          a_spli = a[0].split('.')
                          rangeproxy = f'{a_spli[0]}.{a_spli[1]}.{a_spli[2].strip()}.{rr}'
                          r_url = 'http://'+rangeproxy.strip('\n')+':'+port
                          if len(bughost) == 0:
                              self.w_respon(r_url,rangeproxy,port,bughost,timot,n)
                          else:
                              if 'http://' in bughost or 'https://' in bughost:
                                  self.w_respon(r_url,rangeproxy,port,bughost,timot,n)
                              else:
                                  self.w_respon(r_url,rangeproxy,port,'http://'+bughost,timot,n)
                  self.Hasil()
                elif 'd' == cok:        
                    kopet = open(input('[?] dir range : ')).readlines()
                    port = input(   '[?] port      : ')
                    bughost = input('[?] host      : ')
                    timot = input(  '[?] timeout   : ')
                    mport = port.split(',')
                    n = 0
                    print('CHECKING......')
                    for input_1 in kopet:
                        if '.' in input_1 and len(input_1) < 21:
                            for port in mport:
                                for rr in range(0,255):
                                    n +=1
                                    a = input_1.split('/')
                                    a_spli = a[0].split('.')
                                    rangeproxy = f'{a_spli[0]}.{a_spli[1]}.{a_spli[2].strip()}.{rr}'
                                    r_url = 'http://'+rangeproxy.strip('\n')+':'+port
                                    if len(bughost) == 0:
                                        self.w_respon(r_url,rangeproxy,port,bughost,timot,n)
                                    else:
                                        if 'http://' in bughost or 'https://' in bughost:
                                            self.w_respon(r_url,rangeproxy,port,bughost,timot,n)
                                        else:
                                            self.w_respon(r_url,rangeproxy,port,'http://'+bughost,timot,n)
                    self.Hasil()
                  
                else:
                    exit('pilih \nd = dir \nt = tempel')
                

            elif choose == '2':
                  cok = input('[?] from (d)ir or (t)empel : ')
                  if 't' == cok:
                    input_1 = input('[?] range     : ')
                    port = input(   '[?] port      : ')
                    bughost = input('[?] host      : ')
                    timot = input(  '[?] timeout   : ')
                    mport = port.split(',')
                    n = 0
                    print('CHECKING......')
                    for port in mport:
                        for rr in range(0,255):
                            n +=1
                            a = input_1.split('/')
                            a_spli = a[0].split('.')
                            rangeproxy = f'{a_spli[0]}.{a_spli[1]}.{a_spli[2].strip()}.{rr}'
                            r_url = 'http://'+rangeproxy.strip('\n')+':'+port
                            if len(bughost) == 0:
                                self.no_respon(r_url,rangeproxy,port,bughost,timot,n)
                            else:
                                if 'http://' in bughost or 'https://' in bughost:
                                    self.no_respon(r_url,rangeproxy,port,bughost,timot,n)
                                else:
                                    self.no_respon(r_url,rangeproxy,port,'http://'+bughost,timot,n)
                    self.Hasil()
                  elif 'd' == cok:        
                      kopet = open(input('[?] dir range : ')).readlines()
                      port = input(   '[?] port      : ')
                      bughost = input('[?] host      : ')
                      timot = input(  '[?] timeout   : ')
                      mport = port.split(',')
                      n = 0
                      print('CHECKING......')
                      for input_1 in kopet:
                          if '.' in input_1 and len(input_1) < 21:
                              for port in mport:
                                  for rr in range(0,255):
                                      n +=1
                                      a = input_1.split('/')
                                      a_spli = a[0].split('.')
                                      rangeproxy = f'{a_spli[0]}.{a_spli[1]}.{a_spli[2].strip()}.{rr}'
                                      r_url = 'http://'+rangeproxy.strip('\n')+':'+port
                                      if len(bughost) == 0:
                                          self.no_respon(r_url,rangeproxy,port,bughost,timot,n)
                                      else:
                                          if 'http://' in bughost or 'https://' in bughost:
                                              self.no_respon(r_url,rangeproxy,port,bughost,timot,n)
                                          else:
                                              self.no_respon(r_url,rangeproxy,port,'http://'+bughost,timot,n)
                      self.Hasil()
                    
                  else:
                      exit('pilih \nd = dir \nt = tempel')
            else:
              print('bye x_x')
        except:
          exit('\nexit')

mod = r'''
              $$\                           $$\                           
              $$ |                          $$ |                          
     $$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
    $$  _____|$$  __$$\ $$  __$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
    $$ /      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
    $$ |      $$ |  $$ |$$   ____|$$ |      $$  _$$<  $$   ____|$$ |      
    \$$$$$$$\ $$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
     \_______|\__|  \__| \_______| \_______|\__|  \__| \_______|\__|      
                                                                                                                                              
       [!] Tools   : Range checker     Mode Checking:
       [!] Coder   : bangtebe                 [?] 1. with response
       [!] Version : 1.0                      [?] 2. non response

'''


def main():
    os.system('clear')
    Proxy()
