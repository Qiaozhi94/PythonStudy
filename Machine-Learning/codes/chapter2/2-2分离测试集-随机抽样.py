#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :2-2分离测试集-随机抽样.py
@ Time    :2022/2/14 16:18
@ Author  :qiaozhi94
@ Email   :qiaozhi_li@126.ocm
@ IDE     :PyCharm
"""

# 2-2分离测试集-1.py文件中只是使用了最简单随机的生成方法来分离测试集，这里则采用Scikit-Learn包中的train_test_split（）函数，其与前面定义的
# 函数split_train_test（）几乎相同，除了几个额外特征。首先，它也有random_state参数，让你可以设置随机生成器种子；
# 其次，你可以把行数相同的多个数据集一次性发送给它，它会根据相同的索引将其拆分（例如，当你有一个单独的DataFrame用于标记时，这就非常有用）

from sklearn.model_selection import train_test_split
import pandas as pd

hs = pd.read_csv('housing.csv')
train_set, test_set = train_test_split(hs, test_size=0.2, random_state=50)

print(train_set)
print("-----------------------------------------------------------------------")
print(test_set)

# 这是纯随机的抽样方法，如果数据集足够庞大（特别是相较于属性的数量而言），这种方式通常不错；如果不是，则有可能会导致明显的抽样偏差。
# 2-2分离测试集-分层抽样.py文件中则讲解了分层抽样方法，相比之下会更加准确。
