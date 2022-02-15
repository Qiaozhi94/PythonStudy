#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :2-4可视化训练集数据.py
@ Time    :2022/2/15 12:11
@ Author  :qiaozhi94
@ Email   :qiaozhi_li@126.ocm
@ IDE     :PyCharm
"""

import pandas as pd
import matplotlib.pyplot as plt

hs = pd.read_csv('housing_test.csv')
hs.plot(kind="scatter", x="longitude", y="latitude")  # 根据经纬度画出数据集所分布的位置散点图
hs.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)  # 修改alpha值，可以比较清楚的看到高密度数据点的位置
hs.plot(kind="scatter", x="longitude", y="latitude", alpha=0.05)

hs.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
        s=hs["population"] / 100, label="population", figsize=(10, 7),
        c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True, )
# 使用圆的半径表示人口的多少，圆的颜色表示房价的高低，此时调用一个叫jet的预设颜色表可以画出更加清晰的价格与人口关系的散点分布图

plt.legend()
plt.show()

# 寻找数据相关性
corr_matrix = hs.corr()  # 由于数据集不大，你可以使用corr（）方法轻松计算出每对属性之间的标准相关系数（也称为皮尔逊r）：
print(corr_matrix["median_house_value"].sort_values(ascending=False))
# 查看结果可以看出与median_house_value与各个属性之间的相关性系数分布于1到-1之间, 分别为正相关，不相关与负相关性关系
# median_house_value    1.000000
# median_income         0.688075
# total_rooms           0.134153
# housing_median_age    0.105623
# households            0.065843
# total_bedrooms        0.049686
# population           -0.024650
# longitude            -0.045967
# latitude             -0.144160
# Name: median_house_value, dtype: float64

# 画出收入中位数与房价中位数的散点关系图
hs.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.05)
plt.show()
