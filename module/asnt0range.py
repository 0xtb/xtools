#!user/bin/python

from os import system as cmd
try:
   import random
   import requests as req
except:
      cmd('pip install requests')
      cmd('clear')


h_asn = []
UA = random.choice([ 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3', 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0', 'Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0', 'Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0', 'Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0', 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)', 'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)', 'Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00', 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', 'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14', 'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02', 'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00', 'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)', 'HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 Mobile Safari/534.11+', 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7', 'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5', 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10', 'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27'])

def save(dom):
     if len(h_asn) > 1:
         print('anda mendapat',len(h_asn),'range proxy dari '+dom)
         try:
             saved = input('example: /sdcard/r.txt\n[?] save as: ')
             for w in h_asn:
                 with open(saved,'a') as wr :
                      wr.write(w+'\n')
             print('done !!')
         except:
               exit('error')

def asnLook(dom):
   #dom = input('[?] ASN     : ')
   dom1 = 'AS45671'
   param = 'https://api.hackertarget.com/aslookup/?q={}'.format(dom)
   try:
      resp = req.get(url=param,headers={'User-Agent':UA}).text
      for rep in resp.split('\n'):
          print(rep)
          if '.' in rep and len(rep) < 23:
             h_asn.append(rep)
          else:pass
      save(dom)
   except Exception as err:
         print(err)
   except KeyboardInterrupt:
          save(dom)
          exit('exit')

def asntoprefix(asn):
    #asn= input('[?] ASN    : ')
    url= 'https://api.bgpview.io/asn/'+asn+'/prefixes'
    try:
        res = req.get(url,headers={'User-Agent':UA}).json()
        for i in res['data']['ipv4_prefixes']:
            print(i['prefix'])
            h_asn.append(i['prefix'])
        save(asn)
    except Exception as err:
          print(err)
    except KeyboardInterrupt:
          save(asn)
          exit('exit')



bn = r'''
    
     $$$$$$\   $$$$$$$\ $$$$$$$\  
     \____$$\ $$  _____|$$  __$$\ 
     $$$$$$$ |\$$$$$$\  $$ |  $$ |
    $$  __$$ | \____$$\ $$ |  $$ |
    \$$$$$$$ |$$$$$$$  |$$ |  $$ |
     \_______|\_______/ \__|  \__|

    [?] tools   : Get proxy range
    [?] version : 1.0

'''

def main():
  cmd('clear')
  print(bn)
  try:
      dom = input('[?] ASN     : ')
      h = dom.split(' ')
      if len(dom) == 0:
          exit('bye x_x')
      elif ' v1' in  dom:
          asnLook(h[0])
      elif ' v2' in dom:
          asntoprefix(h[0])
      else:
          asnLook(h[0])
  except Exception as err:
    exit('bye x_x')
