import requests
#r = requests.get("https://movie.douban.com/top250")
r = requests.get("http://www.httpbin.org")
print(r.status_code)




r.encoding = r.apparent_encoding
print(r.text)
#print(r.encoding)







#print(r.headers)