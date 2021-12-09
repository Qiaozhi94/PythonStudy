# 基于session对象实现自动处理
# 如何获取一个session对象：requests.Session()返回一个session对象
# session对象的作用：该对象可以向requests一样调用get和post发起指定的请求，如果在使用session发请求的过程中如果产生了cookie，则cookie会被自动存储在该session对象中，就意味着下次再次使用session对象发起请求，则该次请求就是携带cookie进行的请求发送。
# 在爬虫中使用session的时候，session对象至少会被使用两次：第一次使用session是为了将cookie捕获且保存在session字典中。下次时候就是携带cookie进行的请求发送
# 为什么打印出来是none呢

import requests
hd={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

session = requests.Session()   # 创建session对象
# 第一次使用session对象捕获且存储cookie，猜测对雪球网的首页发起的请求可能会产生cookie
main_url = "https://zhihu.com/"
session.get(main_url,headers=hd)  # 捕获并存储cookie

url = "https://www.zhihu.com/question/395798173"
r = session.get(url,headers=hd,timeout=30)
r.raise_for_status()
r.encoding=r.apparent_encoding
print(r.status_code)
print(r.next)
