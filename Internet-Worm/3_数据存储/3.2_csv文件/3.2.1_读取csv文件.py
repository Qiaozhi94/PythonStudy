import csv

with open('3.2_MoviesTop250_douban.csv','r',encoding='utf-8') as fp:
    # reader其实是一个迭代器
    reader = csv.reader(fp)
    next(reader)  # 如果加上next语句，则i从第一行开始
    for i in reader:
        name = i[1]
        quote = i[-1]
        rating = i[5]
        # print(type(i))
        # print(i)  # 注意：这样的情况是带表头的
        # print({'name':name,'quote':quote,'rating':rating})
# <--------------------分隔符----------------------->
def read_csv_demo():
    with open ('3.2_MoviesTop250_douban.csv','r',encoding='utf-8') as fp:
        # 使用DictReader创建的reader对象，是不包含标题行的
        # reader是一个迭代器，遍历这个迭代器返回来的是一个字典
        reader=csv.DictReader(fp)
        for i in reader:
            value = {"name":i['电影名称'],"year":i['年份']}    # 通过key值获取value的值
            print(value)

if __name__ == '__main__':
    read_csv_demo()