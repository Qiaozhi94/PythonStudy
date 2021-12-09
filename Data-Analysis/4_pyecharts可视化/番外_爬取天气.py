import requests
from lxml import etree
import time
import random
import re
import pandas as pd


def parse_html(each_url):

    hd = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Cookie': 'cityPy=hanzhong; cityPy_expire=1592672836; BAIDU_SSP_lcr=https://www.google.com/; UM_distinctid=172aea65776a2f-0bbcd50b8a9f41-143f6257-1fa400-172aea65777c1c; Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1592068037,1592068065; CNZZDATA1275796416=1072504891-1592065859-https%253A%252F%252Fwww.google.com%252F%7C1592069076; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1592071787'
        }

    r = requests.get(each_url,headers=hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    # print(r.text)
    return r.text




def find_data(html):
    # print(html)
    tree = etree.HTML(html)
    lis = tree.xpath("//div[@class='main clearfix']//div[@class='tian_three']/ul/li")
    for li in lis:
        day = li.xpath(".//div[1]/text()")[0]
        high_tem = li.xpath(".//div[2]/text()")[0]
        low_tem = li.xpath(".//div[3]/text()")[0]
        high_num = re.findall(r"\d+\.?\d*", high_tem)[0]
        low_num=re.findall(r"\d+\.?\d*", low_tem)[0]
        week = day.split(" ")[1]
        yymmdd = day.split(" ")[0]
        # print(yymmdd)
        # print(week)
        # print(high_num)
        # print(low_num)

        site_tem.append([yymmdd,week,high_num,low_num])
        print(site_tem)
        # return site_tem

def save_data(site_tem):

    header=["日期", "星期", "最高气温", "最低气温"]
    test = pd.DataFrame(columns=header,data=site_tem)
    test.to_csv("site_tem.csv",encoding="utf-8")
    print("保存成功！")


if __name__ == '__main__':


    urls = []
    # site = "shanghai"
    site = input("输入要查询的地区：")
    site_tem = []
    original_url="http://lishi.tianqi.com/"
    for year in range(2019,2020):
        if year < 2020:
            for month in range(1,13):
                if month <10:
                    url = original_url + site + "/" + str(year) + str(0) + str(month) + ".html"
                    urls.append(url)
                else:
                    url = original_url + site + "/" + str(year) + str(month) + ".html"
                    urls.append(url)
        else:
            for month in range(1,5):
                url = original_url + site + "/" + str(2020) + str(0) + str(month) + ".html"
                urls.append(url)


    for i in range(len(urls)):
        each_url = urls[i]
        print(each_url)
        time.sleep(random.randint(0,3))

        html = parse_html(each_url)
        find_data(html)
        save_data(site_tem)






