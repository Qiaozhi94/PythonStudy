#利用params拼接url的这个案例的基础之上，想写一个本地端在百度上搜索并返回全部网页数据的脚本


import urllib
import requests
from fake_useragent import UserAgent

name = input("What do you want to search next:")

url = "http://www.baidu.com/s"
params = {
    "wd": name,
    "key": "0",
    "value": "1"
}
str_params = urllib.parse.urlencode(params)
url_new = url+str_params
print("website address:%s" % url_new)

ua = UserAgent()
useragent = ua.random
hd = {"user-agent":useragent}

r = requests.get(url_new,headers=hd)

print("status code:%s" % r.status_code)

r.encoding = r.apparent_encoding
print(r.text)


