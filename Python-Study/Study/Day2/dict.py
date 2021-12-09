'''info = {
    "stu1101": "Qiaozhi li",
    "stu1102": "Lingzi cai",
    "stu1103": "Aaa",
    "stu1104": "Bbb",

}

#print(info)

#print(info["stu1102"])

info["stu1104"] = "xxx"
info["stu1106"] = "lll"

del info["stu1103"]
info.pop("stu1106")

print(info)
'''

av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}


av_catalog["日韩"]["tokyo-hot"][0] = "我还是很喜欢日韩范的"

print(av_catalog)
