import requests

hd={
    'cookie': 'lianjia_uuid=01765a98-5297-41f9-b19d-89a7449cf57a; UM_distinctid=170e7a4b5ffb7b-0fe20ca1f284a2-396d7406-13c680-170e7a4b600ab1; _smt_uid=5e708c78.114db2b5; _ga=GA1.2.1647190516.1584434300; Hm_lvt_efa595b768cc9dc7d7f9823368e795f1=1590328589; select_city=310000; _jzqc=1; _jzqx=1.1584434297.1592370338.8.jzqsr=google%2Ecom|jzqct=/.jzqsr=google%2Ecom|jzqct=/; _jzqckmp=1; _qzjc=1; _gid=GA1.2.427499494.1592370341; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1590290914,1590586455,1590671171,1592370350; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170e7a4bcdc247-0c752ca4b1a414-396d7406-1296000-170e7a4bcddb75%22%2C%22%24device_id%22%3A%22170e7a4bcdc247-0c752ca4b1a414-396d7406-1296000-170e7a4bcddb75%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22office%22%7D%7D; lianjia_ssid=76e8d6d4-eac9-1a36-0a4b-ef77659d303d; CNZZDATA1255604082=1745799172-1588039033-https%253A%252F%252Fwww.google.com%252F%7C1592380486; _jzqa=1.3759888401518846500.1584434297.1592376456.1592381003.29; CNZZDATA1253492439=646215105-1588040561-https%253A%252F%252Fwww.google.com%252F%7C1592381184; CNZZDATA1255633284=1262782669-1588041365-https%253A%252F%252Fwww.google.com%252F%7C1592381302; CNZZDATA1254525948=1479450439-1588037718-https%253A%252F%252Fwww.google.com%252F%7C1592378211; login_ucid=2000000104475969; lianjia_token=2.002814d4ab54c5940639b9fd9a9836d79a; lianjia_token_secure=2.002814d4ab54c5940639b9fd9a9836d79a; security_ticket=euBaN/4SZJwcyvKnJNwHXyEnzh/pmS7jY+fk/AVezXLMuQff2tH7S1H9yliVqRosZRzaHBYRR7x7sqQgCU2oqidJ4fPMtlsePOlcYTIbbyRhLzq1xkb2r59hQHJkl4hjDuQkh9nJQo4uCA9fum2cZaHIb1ZqRr+bVFVuTe2wB+8=; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1592381602; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiOGI3YzExNGQ0NmE0MTdmOTUxYmRhNzFjMDE5OTdjZDIxZWQ3YjUyOGM1MGFiN2MyNmYxODcyYjA2YTYxNmRkNjNlZTYzODE4MTZlYzU3ODU4NWNjYjAyNWEyMjZlNjc3MzM4MDRkZWRiZjhlZmY3Yzg2ZmZjMDBhYmIwNWVhYWRlOTE1YTMwMGQxY2QyZTRiMGI2ZjA2OWE3ZDY2NGNhMTFhNTBjYWMxZWVlOGZhNjdhYzcwYWZmZTgxMDRkMDVjNWI2ZmQ3MWRkZTljNTczNDRiOTYzZDcxZThmODVlYzFhYWY2ZGVmMTUxZTRlN2FlMzQxNTAyNjkwY2EwZTczY2ZmOTE5NTViMWI5NjU5YzUwNjIyMWMyMWQ2OWE3YTU0Y2U0MGZmMzk2M2QzZDEzZGU5YzQxYWRjMmQ5MTIxZmZcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiMmM2ODM1N2FcIn0iLCJyIjoiaHR0cHM6Ly9zaC5saWFuamlhLmNvbS94aWFvcXUvNTAxMTEwMjIwODE5MS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==; _qzja=1.1285165120.1588042706441.1592376455845.1592381003051.1592381603349.1592381604691.0.0.0.137.26; _qzjb=1.1592381003051.9.0.0.0; _qzjto=26.3.0; _jzqb=1.9.10.1592381003.1; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

hd1 = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }

url = 'https://sh.lianjia.com/xiaoqu/5011102208191/'


r = requests.get(url,headers=hd1,timeout=30)
r.raise_for_status()
r.encoding = r.apparent_encoding
print(r.status_code)

# session = requests.Session()
