#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :3.3_Pandas案例movies.py
@ Time    :2020/6/21 5:09 下午
@ Author  :GerorgeL.
@ Email   :George.q.li@outlook.com
@ IDE     :PyCharm
"""
import numpy as np
import pandas as pd

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

file_path = "IMDB-Movie-Data.csv"

data = pd.read_csv(file_path)
print(data)
print(data.info())
print(data.head(1))
print("-"*100)

# 获取电影的平均分
print(data["Rating"].mean())
print("-"*100)

# 获取导演的人数
# set函数让list没有重复的数据，即让列表数据唯一
print(len(set(data["Director"].tolist())))
print(len(data["Director"].unique()))
print("-"*100)
# 两种办法都可以

# 获取演员的信息
temp_actors = data["Actors"].str.split(", ").tolist()
# print(temp_actors)
actors1 = [i for j in temp_actors for i in j]  # 双重循环列表推导式
print(len(set(actors1)))

runtime1 = data["Runtime (Minutes)"].values  # Return Series as ndarray or ndarray-like depending on the dtype
runtime2 = data["Runtime (Minutes)"]
print(runtime1)
print(runtime2)

