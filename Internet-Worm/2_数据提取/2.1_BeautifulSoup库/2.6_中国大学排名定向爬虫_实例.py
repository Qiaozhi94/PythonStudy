#基于BeautifulSoup库的爬取案例
import requests
from bs4 import BeautifulSoup
import bs4




def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "F"

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr("td")  #tr("td")与tr.find_all("td")等价
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "地区", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    #print("suc" + str(num))

def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)    #只列出来前20的大学

main()