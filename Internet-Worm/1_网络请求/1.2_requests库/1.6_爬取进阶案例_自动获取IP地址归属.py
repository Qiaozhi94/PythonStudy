#目前还没有成功，暂不知道是什么问题


import requests

url = "https://www.ip138.com/iplookup.asp?ip="


ipaddr = input("IP address:")
url_input = url + ipaddr
print(url_input)
r = requests.get(url_input)

print(r.status_code)

print(r.text[-500:])