#beautifulsoup库是解析、遍历、维护"标签树"的功能库
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


#with open("demo.html","r",encoding="utf-8") as f:
    #f.read()   这里想调用根目录保存的demo.html，但是不知道是什么原因调用不成功



url = "https://sh.lianjia.com/ershoufang/107102396109.html"
ua = UserAgent()
ua_random = ua.random
hd = {"user-agent":ua_random}
r = requests.get(url,headers = hd)

print(r.status_code)

demo = r.text



soup = BeautifulSoup(demo,"html.parser")

print(soup.title)

tag_a = soup.a
tag_b = soup.b
tag_p = soup.p

print(tag_a)
print(tag_b)
print(tag_p)
