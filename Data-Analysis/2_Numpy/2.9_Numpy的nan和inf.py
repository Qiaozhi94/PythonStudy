import numpy as np

# numpy的nan属性
# 两个nan是互不相等的
a = np.nan
b = np.nan
if a == b:
    print("T")
else:
    print("F")
print("-"*100)

# np.nan != np.nan
if a != b:
    print("T")
else:
    print("F")
print("-"*100)

# 判断数组中nan的个数
c = np.arange(0,20).reshape(4,5)
d = c.astype(float)
d[2,2] = np.nan
d[3,4] = np.nan
d[:,0] = 0
print(d)
print(np.count_nonzero(d!=d))  # 判断数组中nan的个数
print(np.count_nonzero(d))    # 判断数组中不为0的个数
print("-"*100)

# numpy中的运算如果涉及到了nan，则结果必为nan
print(np.sum(d))
print("-"*100)

# 将所有的nan类型替换成0（注意的是，某些情况下不能直接替换成0，因为在求平均值的时候替换成0的结果是数值变小，处理办法是把缺失的数值替换成为均值或中值，或直接删除有缺失值的一行）
d[np.isnan(d)] = 0
print(d)
print("-"*100)

