from bs4 import BeautifulSoup

with open("lianjia_demo.html", "r") as f:
    demo_read = f.read()

#print(demo_read)

soup = BeautifulSoup(demo_read,"html.parser")
#返回一个列表类型，存储查找的结果
#name:对标签名称的检索字符串
for link in soup.find_all("a"):
    print(link.get("href"))



