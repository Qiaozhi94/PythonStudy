#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :1.8_绘制电影时长直方图.py
@ Time    :2020/6/22 10:08 下午
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

runtime = data["Runtime (Minutes)"].values  # Return Series as ndarray or ndarray-like depending on the dtype
max_runtime = runtime.max()
min_runtime = runtime.min()
print(max_runtime)
print(min_runtime)

num_bin = (max_runtime-min_runtime)//5
print(num_bin)

plt.figure(figsize=(20,8),dpi=100)
plt.hist(runtime,num_bin,color="grey")

plt.xticks(range(min_runtime,max_runtime+10,5))


plt.grid()

plt.show()
