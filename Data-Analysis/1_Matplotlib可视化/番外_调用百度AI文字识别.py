from aip import AipOcr
import time
import random





# 读取密码
def getPassword(path="BaiduAI_OCR_My_Password.txt"):
    with open(path, "r", encoding="utf-8") as f:
        APP_ID = f.readline().strip()
        API_KEY = f.readline().strip()
        SECRET_KEY = f.readline().strip()
        print(APP_ID)
        print(API_KEY)
        print(SECRET_KEY)
    return APP_ID, API_KEY, SECRET_KEY




# 打开图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



# 百度AI文字识别
def basicGeneral(file):
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    options = {}
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    result = aipOcr.basicGeneral(file, options)
    return(result)



if __name__ == '__main__':

    APP_ID, API_KEY, SECRET_KEY = getPassword()
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    numbers = []

    for i in range(1, 21):
        filePath = "./pictures/" + str(i) + ".png"

        file = get_file_content(filePath)
        result = basicGeneral(file)
        # print(result)
        for word in result['words_result']:
            a = word['words']

            # print(a)
        numbers.append(a)
        print(numbers)
        time.sleep(random.randint(1, 3))






