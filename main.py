#!/usr/bin/python3

#--  import module
import sys
from module . hostproxy_scanner import main as hpcheck
from module . asnt0range import main as asntrange
from module . range_checker import main as rcheck
from module . port_scanner import main as pcheck
from module . ip_asn import main as iptasn
from os import system as cmd
from module . hostip import main as htip

bnr = r'''
                                                                    
                                                     88             
                     ,d                              88             
                     88                              88             
88,dPYba,,adPYba,  MM88MMM  ,adPPYba,    ,adPPYba,   88  ,adPPYba,  
88P'   "88"    "8a   88    a8"     "8a  a8"     "8a  88  I8[    ""  
88      88      88   88    8b       d8  8b       d8  88   `"Y8ba,   
88      88      88   88,   "8a,   ,a8"  "8a,   ,a8"  88  aa    ]8I  
88      88      88   "Y888  `"YbbdP"'    `"YbbdP"'   88  `"YbbdP"'  

coder         : tebespace
version       : 1.0
list my tools :
                 1. host/proxy check
          	 2. range checker
                 3. port scanner
	         4. asn to range
	         5. host to ip
                 6. ip to asn

'''

def man():
      try:
                cmd('clear')
                print(bnr)
                i = input('choice: ')
                if i == '1':
                   hpcheck()
                elif i == '2':
                     rcheck()
                elif i == '3':
                     pcheck()
                elif i == '4':
                     asntrange()
                elif i == '5':
                     htip()
                elif i == '6':
                     iptasn()
                else:exit('\nbye x_x')
      except:
             exit('\nexit')


if __name__ == '__main__':
   try:
       if len(sys.argv) > 1:
          if sys.argv[1] == '1':
             hpcheck()
          elif sys.argv[1] == '2':
               rcheck()
          elif sys.argv[1] == '3':
               pcheck()
          elif sys.argv[1] == '4':
               asntrange()
          elif sys.argv[1] == '5':
               htip()
          elif sys.argv[1] == '6':
               iptasn()
          else:
               print('''
         use:
               1  :  host/proxy check
               2  :  range checker
               3  :  port scanner
               4  :  asn to range
               5  :  host to ip
               6  :  ip to asn''')
       else:man()
   except:exit('\nkeluar')



