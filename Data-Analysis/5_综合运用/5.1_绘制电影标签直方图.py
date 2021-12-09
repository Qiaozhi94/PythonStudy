#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :5.1_绘制电影标签直方图.py
@ Time    :2020/6/22 11:04 下午
@ Author  :GerorgeL.
@ Email   :George.q.li@outlook.com
@ IDE     :PyCharm
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)


file_path ="/Users/georgel./Files/Study-Notes/Python/数据分析/3_Pandas/IMDB-Movie-Data.csv"
data = pd.read_csv(file_path)
print(data.head(1))
print(data.shape[0])



# 统计分类的列表
temp_genre = data["Genre"].str.split(",").tolist()
print(temp_genre)  # 嵌套列表的形式

# set()的作用就是使列表元素唯一化
genre_list = list(set(i for j in temp_genre for i in j))  # 双重列表推导式将嵌套列表两次遍历进入一个大列表
print(genre_list) # 所有电影的种类集合列表，没有重复的元素

# 将字符串转换为数据，这个方法十分重要（也可以使用value_counts方法）
# 构造全为0的数组
zeros_data = pd.DataFrame(np.zeros((data.shape[0],len(genre_list))),columns=genre_list)
# zero()的函数构造的是一维数组，则是一个括号；如果是二维数组，则是两个括号；如果是三位数组，则是三个括号
# print(zeros_data)

# 给每个电影出现分类的位置赋值为1
for i in range(data.shape[0]):
    zeros_data.loc[i,temp_genre[i]] = 1
print(zeros_data)

# 统计每个分类的电影的数量和
sum_genre = zeros_data.sum(axis=0)
print(sum_genre)

# 排序
sum_genre= sum_genre.sort_values()
print(sum_genre)
print(type(sum_genre))

# 开始绘制直方图
plt.figure(figsize=(20,15),dpi=100)


_x = sum_genre.index
_y = sum_genre.values

plt.bar(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x)


plt.grid()

plt.show()

