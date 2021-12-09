import requests
#网络链接有风险
#异常处理很重要



url = "http://httpbin.org/"


try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()  #如果返回的代码不是200，表明信息并没有正确获得，将产生一次异常
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("产生异常")