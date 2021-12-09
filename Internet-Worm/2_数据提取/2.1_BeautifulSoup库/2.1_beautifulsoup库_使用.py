#beautifulsoup库是可以解析html和xml文件的功能库
#beautifulsoup库是解析、遍历、维护"标签树"的功能库

import requests
from bs4 import BeautifulSoup
#from fake_useragent import UserAgent

url = "https://sh.lianjia.com/ershoufang/107102396109.html"
#ua = UserAgent()
#ua_random = ua.random
#hd = {"user-agent":ua_random}
#r = requests.get(url,headers = hd)
r = requests.get(url)

print(r.status_code)

demo = r.text

with open("lianjia_demo.html", "w", encoding="utf-8") as f:
    f.write(demo)


soup = BeautifulSoup(demo,"html.parser")

print(soup.prettify)