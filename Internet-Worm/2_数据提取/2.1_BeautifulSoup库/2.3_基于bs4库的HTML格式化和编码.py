
demo = "lianjia_demo.html"

from bs4 import BeautifulSoup


with open(demo, "r") as f:
    demo_read = f.read()

print(demo_read)

soup = BeautifulSoup(demo_read,"html.parser")
print(soup.title)
print(soup.title.prettify())
#prettify起到的是HTML格式化和美化的作用
