#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :独热编码与标签编码示例.py
@ Time    :2020/6/22 11:17 下午
@ Author  :GerorgeL.
@ Email   :George.q.li@outlook.com
@ IDE     :PyCharm
"""

# 首先了解机器学习中的特征类别：连续型特征和离散型特征
# 对于离散性特征：Binarize categorical/discrete features: 对于离散的特征基本就是按照one-hot（独热）编码，该离散特征有多少取值，就用多少维来表示该特征。

# 独热码，在英文文献中称做 one-hot code, 直观来说就是有多少个状态就有多少比特，而且只有一个比特为1，其他全为0的一种码制。
# 自然状态码为：000,001,010,011,100,101
# 独热编码为：000001,000010,000100,001000,010000,100000
# 独热编码的优缺点：
# 优点：独热编码解决了分类器不好处理属性数据的问题，在一定程度上也起到了扩充特征的作用。它的值只有0和1，不同的类型存储在垂直的空间。
# 缺点：当类别的数量很多时，特征空间会变得非常大。在这种情况下，一般可以用PCA来减少维度。而且one hot encoding+PCA这种组合在实际中也非常有用。


# 独热编码如下:
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
enc = preprocessing.OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])    # fit来学习编码
print(enc.transform([[0, 1, 3]]).toarray())    # 进行编码


# 输出：array([[ 1., 0., 0., 1., 0., 0., 0., 0., 1.]])
# 数据矩阵是4*3，即4个数据，3个特征维度。
# 观察左边的数据矩阵，第一列为第一个特征维度，有两种取值0\1. 所以对应编码方式为10 、01
# 同理，第二列为第二个特征维度，有三种取值0\1\2，所以对应编码方式为100、010、001
# 同理，第三列为第三个特征维度，有四中取值0\1\2\3，所以对应编码方式为1000、0100、0010、0001
# 再来看要进行编码的参数[0 , 1, 3]， 0作为第一个特征编码为10, 1作为第二个特征编码为010， 3作为第三个特征编码为0001. 故此编码结果为 1 0 0 1 0 0 0 0 1

# 标签编码如下：
le = LabelEncoder()
le.fit([1,5,67,100])
print(le.transform([1,1,100,67,5]))

le = preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])
LabelEncoder()
print(list(le.classes_))
# 三个类别分别为0 1 2
print(le.transform(["tokyo", "tokyo", "paris"]))
print(list(le.inverse_transform([2, 2, 1])) )  # 逆过程

# 限制：上文颜色的例子已经提到标签编码了。Label encoding在某些情况下很有用，但是场景限制很多。再举一例：比如有[dog,cat,dog,mouse,cat]，我们把其转换为[1,2,1,3,2]。这里就产生了一个奇怪的现象：dog和mouse的平均值是cat。所以目前还没有发现标签编码的广泛使用。

