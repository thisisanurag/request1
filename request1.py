import requests
import time
url='http://www.google.com'
l=[
'90.178.25.224:60737',
'178.216.0.168:33364',
'150.107.206.249:61954',
'46.227.169.206:8888',
'70.169.129.235:48678',
'201.87.154.127:8080',
'134.249.149.219:35795',
'117.7.230.113:443',
'49.156.37.20:8080',
'115.85.65.94:8080',
'103.93.136.8:8080',
'90.188.35.190:8080',
'95.86.133.70:8080',
'190.248.153.162:8080',
'202.152.142.234:3128',
'177.12.82.181:8080',
'91.225.5.43:59039',
'159.224.182.206:46497',
'188.136.223.163:8888',
'122.55.250.90:8080',
'46.229.206.135:39083',
'47.89.37.177:3128']
c=0
for x in l:
    x.strip()

    proxies= {'http': x,
                'https': x}
    s=requests.Session()
    s.proxies=proxies
    try:
        r=s.get(url)
        c+=1
        print(x,'   count=',c)
    except:
        print('error')
    #print(r.text)
