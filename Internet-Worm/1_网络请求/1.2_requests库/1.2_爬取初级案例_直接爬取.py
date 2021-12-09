import requests
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context
url1 = "https://www.bilibili.com/video/BV1yp4y1X7Xw"
url2 = "https://sh.lianjia.com/ershoufang/107102396109.html"
url3 = "https://sh.lianjia.com/ershoufang"

try:
    r = requests.get(url3)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    print(r.text)
    print(r.request.headers)
except:
    print("产生异常")