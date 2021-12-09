import requests
import re

hd = {
        'authority': 'search.jd.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'referer': 'https://message.bilibili.com/pages/nav/index_new_pc_sync',
        'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
        'cookie': "shshshfpa=4792a6e6-49c8-6a51-d334-c5ce0355d463-1580913904; shshshfpb=w9ovlvmUzcLLsZ%2FwKfdQuxA%3D%3D; TrackID=15BeYqWvUKwsxqMdjOcDiPODyhSuQ2QrQFctpDk5eSJv6Q5cnGb4mjxdRW5K_DSePiEzyaiEhtS-TcVP8Qwdr0eqL4kL1amoLFzLaCSQ-4ZYytivV2ub3uIfXcJoOuEEf|||wITFwODTMir5SqZwHpeUdA; pinId=wITFwODTMir5SqZwHpeUdA; __jdu=15784095964071777510493; areaId=27; ipLoc-djd=27-2442-2444-0; unpl=V2_ZzNtbUMFEUEmDhMBch5ZUWILQV8SUkMQd1tABnNKXgI0AhYJclRCFnQUR1BnGVwUZwcZXUZcQBxFCEdkeB5fA2AFEFlBZxVLK14bADlNDEY1WnwHBAJfF3ILQFJ8HlQMZAEUbXJUQyV1CXZUfx9VAGYLFlVFUkITdQ5AUn8ZXQBvASJtRWdzJXMBRlZ%2fGGwEVwIiHxYLRBJyDUVUNhlYA24GE1VGX0QQdA5GUn0fWAVmBhpfclZzFg%3d%3d; __jdv=76161171|google-search|t_262767352_googlesearch|cpc|kwd-362776698237_0_0cceb7dd864e49b3a4143b7c9b36b05e|1589181328947; PCSYCityID=CN_610000_610700_610722; __jda=122270672.15784095964071777510493.1578409596.1589127918.1589181329.21; __jdc=122270672; shshshfp=f5fdc3bdbabc6f36173353df0d18aa5d; 3AB9D23F7A4B3C9B=PV6RA2MKMWDFPMQAGQ54B6EXQGZHLTBWDGXT3J4T2D7BJGFZW5YYP77CNUB4G47G2IE5Z3GYCJDEFGHDOURYR35IXQ; qrsc=3; __jdb=122270672.4.15784095964071777510493|21.1589181329; shshshsID=805b0a620b6ee04a5a6aad3772a65244_4_1589181361031; rkv=V243259235108",
    }


def get_html_text(url_new):
    try:
        r = requests.get(url_new, headers =hd, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

def parse_page(list,html):
    pass
    #try:




print("")




def print_list(info_list):
    print("")





def main():
    goods = "资本论"
    start_url = "https://search.jd.com/Search?keyword=" + goods
    depth = 3
    info_list= []
    for i in range(depth):
        try:
            url = start_url +'&page=' +str(2*i-1) + '&s=' +str((2*i-1)*30)
            html = get_html_text(url)
            parse_page(info_list, html)
        except:
            return "爬取失败"
    print_list(info_list)


main()




