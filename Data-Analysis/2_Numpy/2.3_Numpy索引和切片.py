import numpy as np
# 读取csv文件
a = np.loadtxt("data.csv",delimiter=",",dtype="int",skiprows=1)
print(a)
print("-"*100)

# 数组取单行
print(a[2])
print(a[True,True])
print("-"*100)

# 数组取连续多行
print(a[2:])
print("-"*100)

# 数组取不连续多行
print(a[[2,8,11]])
print("-"*100)

# 数组取列
print(a[:,2])
print("-"*100)

# 数组取连续的多列
print(a[:,2:])
print("-"*100)

# 数组取不连续的多列
print(a[:,[1,3]])
print("-"*100)

# 数组取行和列
print(a[2,3])
print("-"*100)
print(a[[2,5,8],[0,2,2]])
print(type(a[2,3]))
print("-"*100)

# 数组取多行和多列，取第三行和第五行，第二列到第四列的结果
print(a[2:5,1:4])

