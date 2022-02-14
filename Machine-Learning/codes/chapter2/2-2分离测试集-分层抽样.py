#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :2-2分离测试集-分层抽样.py
@ Time    :2022/2/14 16:56
@ Author  :qiaozhi94
@ Email   :qiaozhi_li@126.ocm
@ IDE     :PyCharm
"""

# 本次尝试使用分层抽样方法替代随机抽样方法，这里采用收入中位数这一重要属性来衡量放家中位数。
# 目标是希望确保在收入属性上，测试集能够代表整个数据集中各种不同类型的收入。


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hs = pd.read_csv('housing.csv')
hs["income_column"] = pd.cut(hs["median_income"], bins=[0., 1.5, 3.0, 4.5, 6., np.inf], labels=[1, 2, 3, 4, 5])
# np.inf表示无穷大的意思
hs["income_column"].hist()
plt.show()  # 先将数据集的收入中位数按照前后顺序分为六组
