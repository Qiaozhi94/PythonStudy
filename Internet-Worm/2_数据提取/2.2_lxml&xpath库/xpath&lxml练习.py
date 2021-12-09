import requests
from lxml import etree

# url="https://sh.lianjia.com/ershoufang/pg1/"
#
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     html = r.text
#     # print(html)
#     with open("lianjia.html","w") as f:
#         f.write(html)
#
# except:
#     print("爬取失败")



parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('lianjia.html', parser=parser)

# prices =html.xpath("//div//li/div/div/div[@class='totalPrice']/span[@class='xh-highlight']/text()")
# prices =html.xpath("//div//li/div/div/div[@class='totalPrice']/span")
prices =html.xpath("//div//li/div/div/div[@class='totalPrice']/span/text()")
print(prices)

unitprices = html.xpath("//div//div[@class='unitPrice']/span/text()")
print(unitprices)
names = html.xpath("//div//div//a[@class='title']//text()")
print(names)
# for Price in prices:
#     Price_str = etree.tostring(Price,encoding='utf-8').decode("utf-8")
#     print(Price_str)





# for Unitprices in unitprices:
#     Unitprice_str = etree.tostring(Unitprices,encoding='utf-8').decode("utf-8")
#     print(Unitprice_str)
#
# for Names in names:
#     Name_str = etree.tostring(Names,encoding='utf-8').decode("utf-8")
#     print(Name_str)




# 价格：//div//li/div/div/div[@class='totalPrice']/span
# 单价：//div//div[@class='unitPrice']
# 名字：//div//div//a[@class='title']
# 编号：//div/div/div/a[@class='title']/@data-housecode
# 位置：//div//div[@class='positionInfo']
# 属性：//div//div[@class='houseInfo']
# 关注：//div//div[@class='followInfo']