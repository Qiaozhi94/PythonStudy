import re
from bs4 import BeautifulSoup

with open("lianjia_demo.html", "r") as f:
    demo_read = f.read()

soup = BeautifulSoup(demo_read,"html.parser")




for tag in soup.find_all(re.compile("b")):
    print(tag.name)  #对标签名称的检索字符串

for tag in soup.find_all(re.compile("link")):
    print(tag)

#attrs：对标签属性值的检索字符串，可标注属性检索
#recursive：是否对子孙全部检索，默认true
#string：<>...</>中字符串区域的检索字符串
#<tag>(...)等价于<tag>.fina_all(...)

#-扩展方法-#
#<>.find()  搜索且只返回一个结果，字符串类型，同.find_all()参数
#<>.find_parents  在先辈节点中搜索，返回列表类型，同.find_all()参数
#<>.find_parent()  在先辈节点中返回一个结果，字符串类型，同.find()参数
#<>.find_next_siblings()  在后续平行节点中搜索，返回列表类型，同.find_all()参数
#<>.find_next_sibling()   在后续平行节点中返回一个结果，字符串类型，同.find()参数
#<>.find_previous_siblings()  在前序平行节点中搜索，返回列表类型，同.find_all()参数
#<>.find_previous_sibling()   在前序平行节点中返回一个结果，字符串类型，同.find()参数