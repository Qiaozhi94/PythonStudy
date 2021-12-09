1. get传参

(1) 汉字报错：解释器ASCII没有汉字，采用url汉字转码

~~~python
urllib.parse.quote  safe='string.printable'
~~~

(2) 字典传参

~~~python
Urllib.parse.urlencode()
~~~

post请求：

~~~python
Urllib.request.openurl(url,data = "服务器接受的数据")
~~~

---

handler处理器的自定义：

