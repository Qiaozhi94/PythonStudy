#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :3.2_Pandas的DataFrame.py
@ Time    :2020/6/19 5:05 下午
@ Author  :GerorgeL.
@ Email   :George.q.li@outlook.com
@ IDE     :PyCharm
"""
import pandas as pd
import numpy as np


# pandas文件的DataFrame
# DataFrame是一个Series容器
data1 = np.arange(12).reshape(3,4)
data2 = np.arange(12).reshape(3,4)
pd_df1 = pd.DataFrame(data1,index=list("abc"),columns=list("wxyz"))
pd_df2 = pd.DataFrame(data2)
print(pd_df1)
print("-"*100)
print(pd_df2)
print("-"*100)
# DataFrame对象既有行索引，又有列索引
# 行索引，表明不同行，横向索引，称为row，0轴，axis=0
# 列索引，表明不同列，纵向索引，称为columns，1轴，axis=1


# 创建pandas的DataFrame的各种方式
data3 = [{"name":"xiaozhang","age":32,"tel":10010},{"name":"xiaowang","tel":10086},{"name":"xiaoli"}]
pd_df3 = pd.DataFrame(data3)
print(pd_df3)
print("-"*100)
data4 = {"name":["xiaoming","xiaozhang","xiaowang"],"age":[20,32,40],"tel":[10010,10086,10001]}
pd_df4 = pd.DataFrame(data4)
print(pd_df4)
print("-"*100)

# DataFrame的基本属性
# df.shape 行数 列数
# df.dtypes 列数据类型
# df.ndim 数据维度
# df.index 行索引
# df.columns 列索引
# df.values 对象值 二维ndarray数组

# DataFrame整体情况查询
# df.head() 显示头部几行，默认5行
# df.tail() 显示末尾几行，默认5行
# df.info() 相关信息概览：行数，列数，列索引，列非空值个数，列类型，内存占用
# df.describe() 快速综合统计结果：计数，均值，标准差，最大值，四分位数，最小值

# DataFrame的info及describe
data5 = pd.read_csv('USvideos.csv')
print(data5.info())
print("-"*100)
print(data5.describe())
print("-"*100)

# DataFrame中的切片和索引
print(data5[:20])
print("-"*100)
print(data5[:20]["views"])
print("-"*100)
# 方括号写数字，表示取行，对行进行操作
# 方括号写字符串，表示取列，对列进行操作

# 还有更多经过pandas优化过的选择方式
# df.loc 通过标签索引行数据，就是取数
# df.iloc 通过位置获取行数据，就是取数
data6 = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
print(data6)
print(type(data6.loc["a","z"]))
print(data6.loc["a"])
print(data6.loc[:,"y"])
print(data6.loc[["a","c"]])
print(data6.loc[["a","b"],["x","z"]])
print(data6.loc["a":"c",["w","z"]])   # 冒号在loc里面是闭合的，即会选择到冒号后面的数据
print(data6.iloc[1])
print(data6.iloc[1,:])
print(data6.iloc[:,2])
print(data6.iloc[:,[2,1]])
print(data6.iloc[[0,2],[2,1]])
print("-"*100)

# pandas中是自动转换成为float然后赋值成为nan的
data6.iloc[1:,:2] = np.nan
print(data6)
print("-"*100)

# pandas的布尔索引
data7 = pd.DataFrame(np.arange(24).reshape(4,6),index=list("abcd"),columns=list("uvwxyz"))
data8 = data7[(data7["y"]>12)&(data7["z"]<20)]  # &且
data9 = data7[(data7["y"]>12)|(data7["z"]<20)] # |或
print(data8)
print("-"*100)
print(data9)

# pandas中缺失数据的处理
print(data6)
print("-"*100)
# NaN的查找
print(pd.isnull(data6))
print("-"*100)
# NaN的删除
print(data6.dropna(axis=0,how="any",inplace=False))
print("-"*100)
# NaN的填充
print(data6.fillna(20))
print("-"*100)
print(data6.fillna(data6.mean()))
# pandas中计算均值等常见数据计算是会把NaN跳过的