#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :3.1_Pandas基础.py
@ Time    :2020/6/18 10:46 下午
@ Author  :GerorgeL.
@ Email   :George.q.li@outlook.com
@ IDE     :PyCharm
"""


import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# 将一段列表转换成为pandas中的Series
a = np.arange(1,20)
print(a)
print("-"*100)
b = pd.Series(a)
print(b)
print(type(b))
print(b.dtype)
print("-"*100)

# 在Series中添加index索引部分，用于修改默认索引
c = pd.Series(a,index=range(1,20))
print(c)
print("-"*100)

# 将字典转换成为Series，其中字典中的键成为索引部分
d = {"name":"george","age":"26","address":"china"}
e = pd.Series(d)
print(e)
print("-"*100)

# Series的索引和切片
print(e["age"])
print(c[15])
print(c[10:])
print(c[[1,3,6]])
print(e.index)
print(len(e.index))
print(list(e.index))  # 可以强制转换成为list类型
print(list(e.index)[1])
print(c.index)
print(e.values)
print(type(e.values))
print("-"*100)
# ndarray的很多方法都可以运用于series类型，比如argmax,clip
# series具有where方法，但是结果和ndarray不同


# pandas读取csv中的文件
f1 = pd.read_csv('USvideos.csv')
f2 = pd.read_csv("/Users/georgel./Files/Study-Notes/Python/爬虫学习/上海小区list.2020.06.17.17.49.03.csv")
print(f1)
print("-"*100)
print(f2)
print("-"*100)

# pandas读取Excel文件
data = pd.read_excel("USvideos.xlsx",sheet_name='data')
writer = pd.ExcelWriter("data.xlsx")
data.to_excel(writer,sheet_name="data_pandas",index=False)
writer.save()
print("-"*100)

# pandas将csv文件转存为Excel文件
csv = pd.read_csv('USvideos.csv')
csv.to_excel("USvideos.xlsx",sheet_name='data')
print("-"*100)

# pandas将Excel文件转存为csv文件
data = pd.read_excel("USvideos.xlsx",sheet_name='data')
data.to_csv("data.csv")
print("-"*100)

# pandas将csv文件中的数据存入mysql中
# engine = create_engine('mysql+pymysql://root:liqiaozhi1994@localhost:3306/USvideosdb')
# data = pd.read_csv('USvideos.csv',sep=",")
# data.to_sql("videopg",engine,index=False)
# print("Write to MySQL successfully!")
# print("-"*100)

# pandas读取mysql数据库数据
# engine = create_engine('mysql+pymysql://root:liqiaozhi1994@localhost:3306/USvideosdb')
# sql = """
#       select * from videopg;
#       """
# data = pd.read_sql_query(sql,engine)
# print(data)
# print("Read the MySQL table successfully!")


