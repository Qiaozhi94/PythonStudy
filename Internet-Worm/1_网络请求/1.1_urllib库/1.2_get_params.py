import urllib.request
import urllib.parse    #转译汉字
import string     #转译汉字
import ssl   #导入ssl跳过证书验证过程
ssl._create_default_https_context = ssl._create_unverified_context


def get_method_params():
    url = "https://www.baidu.com/s?wd="
    name = "名人"   #拼接字符串
    final_url = url+name
    print(final_url)
    encode_new_url = urllib.parse.quote(final_url,safe=string.printable)
    #python是解释性语言，解析器只能识别ASCII码，即不支持中文。这里需要转译汉字成ASCII码
    print(encode_new_url)
    response = urllib.request.urlopen(encode_new_url)
    print(response)

    data_new= response.read().decode()
    print(data_new)    #解码结果成为UTF-8格式

    with open("1-2encode.html", "w", encoding="utf-8")as f:
        f.write(data_new)








get_method_params()  #调用函数