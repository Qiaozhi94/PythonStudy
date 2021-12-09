import numpy as np
import random
np.set_printoptions(suppress=True)  # 解决ndarray默认使用科学计数法显示的问题

# 数组整体求和及分体求和
a = np.loadtxt("USvideos.csv",delimiter=",",dtype=int,skiprows=1)
print(a)
print("-"*100)
print(np.sum(a,axis=0))
print("-"*100)

# 求数组每列数据的平均值或中值
b = (np.sum(a,axis=0))/len(a[:,0])
c = np.mean(a[:,0])
d = a.mean(axis=0)
print(b)  # 求数组每列数据的平均值
print("-"*100)
print(c)  # 求数组第一列数据的平均值
print("-"*100)
print(d)  # 求数组
print("-"*100)

# 求数组中的最大值和最小值
print(a.max()) # 求数组中所有数中的最大值
print(a.max(axis=0))  # 求数组中每行中的最大值
print(a.min())  # 求数组中所有数中的最小值
print(a.min(axis=1))  # 求数组中每列中的最小值
print("-"*100)

# 求数组中的标准差(标准差是一组数据平均值分散程度的一种衡量。一个较大的标准差代表着大部分数值和气平均值之间相差较大）
print(a.std(axis=1))
print(a.std())
e = (a.std(axis=1)/(a.std()))
print(e)  # 推测e可以用来反应每个数值的离散程度
print("-"*100)

# 寻找数组中的nan并且替换成平均值
a = a.astype(float)
for i in range(0,random.randint(0,20)):
    a[(random.randint(400,1000)),(random.randint(0,4))] = np.nan

print(a)
print(a.shape[0])
print("-"*100)
print(np.count_nonzero(a!=a))  # 数组中nan的个数
print("-"*100)

for i in range(0,a.shape[0]):
    temp_col = a[i,:]
    nan_num = np.count_nonzero(temp_col!=temp_col)
    if nan_num != 0:
        print(i)
        not_nan_col = temp_col[temp_col==temp_col]
        temp_aver = not_nan_col.mean()
        temp_col[np.isnan(temp_col)] = temp_aver

    else:
        pass

print(a)


