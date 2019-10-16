import requests
url='http://www.google.com'
#Enter the proxy to be used
proxies= {'http': 'http://0.0.0.0:80',
          'https': 'https://0.0.0.0:80'}
s=requests.Session()
s.proxies=proxies
r=s.get('https://www.google.com')
print(r.text)
