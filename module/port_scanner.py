#!/usr/bin/python3

from os import system as cmd
try:
	import requests as r
except:
	cmd('pip3 install requests')


r200 = []

def save():
     if len(r200) > 0:
         print('anda mendapat',len(r200))
         try:
             saved = input('example: /sdcard/r.txt\n[?] save as: ')
             for w in r200:
                 with open(saved,'a') as wr :
                      wr.write(w+'\n')
             print('done !!')
         except Exception as err:
               print('ERR: \n',err)
     else:
     	exit('anda kurang bruntung kali ini x_x')

def cecker(proxy,port,timot,n):
	try:
		r_url = 'http://'+str(proxy)+':'+str(port)
		res = r.get(r_url,timeout=int(timot),allow_redirects=False)
		print(f'\nLine           : {n}')
		print('Status         : CONNECTED')
		print(f'Proxy & Port   : {proxy}:{port}')
		print(f'Response       : {res.status_code}\n')
		r200.append(f'{proxy}:{port} Response: {res.status_code}')

	except Exception as err:
		# print(err)
		print(f'Line           : {n}')
		print('Status         : CLOSED')
		print(f'Proxy & Port   : {proxy}:{port}\n')
	except KeyboardInterrupt:
		save()
		exit()


def scn():
	proxy = input('[?] tempel    : ')
	timot = input(  '[?] timeout   : ')
	p_port = input('[?] port (r)ange or (n)ot ?  ')
	if p_port == 'r':
	  s = int(input('[?] start     : '))
	  f = int(input('[?] fhinish   : '))
	  th = int(input('[?] loncatan  : '))
	  f = f + 1
	  n = 0
	  print('CHECKING .......')
	  for port in range(s,f,th):
	  	  n += 1
	  	  cecker(proxy,port,timot,n)
	  save()

	elif p_port == 'n':
		port = input(   '[?] port      : ')
		ports = port.split(',')
		n = 0
		print('CHECKING .......')
		for port in ports:
			n +=1
			cecker(proxy,port,timot,n)
			
	else:
		exit('use:\nr = range\nn = not')

bnr = r'''

                               $$\ 
                               $$ |                                  
 $$$$$$\   $$$$$$\   $$$$$$\ $$$$$$\    $$$$$$$\  $$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\\_$$  _|  $$  _____|$$  _____|$$  __$$\ 
$$ /  $$ |$$ /  $$ |$$ |  \__| $$ |    \$$$$$$\  $$ /      $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |       $$ |$$\  \____$$\ $$ |      $$ |  $$ |
$$$$$$$  |\$$$$$$  |$$ |       \$$$$  |$$$$$$$  |\$$$$$$$\ $$ |  $$ |
$$  ____/  \______/ \__|        \____/ \_______/  \_______|\__|  \__|
$$ |                                                                 
$$ |                                                                 
\__|    

	     [?] tools: port scanner  [?] version: 1.0
	     [?] coder: bangtebe

'''


def main():
	try:
            cmd('clear')
            print(bnr)
            scn()
	except:
              exit('\nexit')
