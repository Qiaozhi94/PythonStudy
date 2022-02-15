#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :2-3分离测试集-0.py
@ Time    :2022/2/11  15:00
@ Author  :qiaozhi94
@ Email   :qiaozhi_li@126.ocm
@ IDE     :PyCharm
"""
import pandas as pd
import numpy as np

# 分步熟悉阶段
a = np.random.permutation(10)  # 输入一个数，结果是生成一个随机序列
arr1 = np.arange(9).reshape((3, 3))  # 输入一个数组，结果是生成一个数组的随机序列
b = np.random.permutation(arr1)
print(a)  # 生成了一个随时序列
print(arr1)  # 快速生成一个三维数组
print(b)  # 和arr结果对比可知，permutation函数只对数组第一维进行打乱
print("----------------------------------------")
c = a[:3]  # 选取随机序列a中的前三个数字成为单独的数组
d = a[5:]  # 选取随机序列a中的后五个数字成为单独的数组
print(c)
print(d)
print("----------------------------------------")

arr2 = pd.DataFrame(np.arange(16).reshape(4, 4), index=list('abcd'), columns=list('ABCD'))
print(arr2)
print(arr2.loc['a'])  # 取索引为'a'的行
print(arr2.iloc[0])  # 取第一行数据，索引为'a'的行就是第一行，所以结果与上面的相同
print(arr2.loc[:, ['A']])  # 取'A'列所有行，多取几列格式为 data.loc[:,['A','B']])
print(arr2.iloc[:, [0]])  # 取第0列所有行，多取几列格式为 data.iloc[:,[0,1]])


# 完整代码阶段
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))  # 输入数据集的实例总数随机生成一个随机序列（见分步熟悉阶段）
    test_set_size = int(len(data) * test_ratio)  # 输入比例后得出测试集的实例数
    test_indices = shuffled_indices[:test_set_size]  # 按照测试集的大小选取随机虚列的前xx位数字标签
    train_indices = shuffled_indices[test_set_size:]  # 选取出测试集之后剩下的数字标签所对应的数据即为训练集的数据
    return data.iloc[train_indices], data.iloc[test_indices]  # 根据所选择的数字标签分别摘录出测试集与训练集的数据


hs = pd.read_csv('housing.csv')
train_set, test_set = split_train_test(hs, 0.2)
print(train_set)
print(len(train_set))
print(test_set)
print(len(test_set))
