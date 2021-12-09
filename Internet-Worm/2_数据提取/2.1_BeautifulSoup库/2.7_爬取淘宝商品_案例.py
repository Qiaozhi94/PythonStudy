import requests
import re


def getHTMLText(url):
    try:
        headers = {
            'authority': 's.taobao.com',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306',
            'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
            'cookie': 'cna=BIpSFsUTxg0CAXNBFGQAkQLz; thw=cn; tracknick=aptx4869%5Cu9F2C; miid=611778661056105987; lgc=aptx4869%5Cu9F2C; tg=0; enc=cJ2%2F1XapqPzJz%2FvudG7E6cEfjLmZRbeEHVmudCpoVzTEV0kSn%2FhLhE8Ng8S%2BUAs9HdFnZtciySm4h3smJgH%2FfA%3D%3D; _fbp=fb.1.1585922001529.1067420303; hng=CN%7Czh-CN%7CCNY%7C156; t=5b2c8014c3d00f6c2cd2822377656ba5; cookie2=5cb6c98638f021c1136cc39a6578d3a2; v=0; _tb_token_=f393b63db6519; alitrackid=www.taobao.com; _samesite_flag_=true; dnk=aptx4869%5Cu9F2C; mt=ci=107_1; tfstk=cwRRBF1YBqURT6TPQBHcOdAVXI0GZ1MAY8sg92MeWZNZK1PditAM6dmmPNZRMqC..; lastalitrackid=www.taobao.com; sgcookie=Ec11mbKTWP%2BgNgj2bmBF4; uc3=nk2=AmHtgoHqrqBGgg%3D%3D&id2=UoH4EzT7snhwZg%3D%3D&vt3=F8dBxGXOk%2FrtL5UtWaw%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; csg=8569f8fc; skt=f97d6f4902d60c57; existShop=MTU4ODY1NTE2Ng%3D%3D; uc4=nk4=0%40AIpxstTdO1cFnfPBDNurjckRlbGf&id4=0%40UOnnFuz64k%2FXQiAhTry1QgeAOGGo; _cc_=V32FPkk%2Fhw%3D%3D; _m_h5_tk=e804abad98e2a9efaf44af1b0bce3f06_1588663087472; _m_h5_tk_enc=fad50af1f3e5bb7e101b45bc5c994bd3; uc1=existShop=false&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cart_m=0&cookie14=UoTUMtdfe%2BbTlw%3D%3D&tag=8&lng=zh_CN&pas=0&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D; JSESSIONID=F2092BB2A3F99E5C92CF6000AB717B36; isg=BK-vcE7JLZQ42CrXvToM1hvgPsW5VAN2XhsMY8E8zp4lEMwSySeYxvACkgAuaNvu; l=eB_OIPlnqezH9v62BO5Nourza77tiIRf1sPzaNbMiIHca69NtFGb5NQcubfBSdtjgtfYOetP8XiKbRUJSN4Zw2HvCbKrCyClExJGR',
        }

        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\":\"[\d+\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("F")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = 'ps4 pro'
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()
