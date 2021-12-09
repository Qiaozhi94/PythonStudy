import requests
from fake_useragent import UserAgent
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

ua = UserAgent()
url1 = "http://www.amazon.cn/dp/B07GPZBVZT/"
url2 = "http://www.baidu.com"

hd = {"user-agent":ua}

print(hd)
#hd = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
#hd = {"user-agent":"Mozilla/5.0"}
print(ua.random)

try:
    r = requests.get(url1,headers = hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    print(r.text)
    #print(r.request.headers)
except:
    print("爬取失败")
