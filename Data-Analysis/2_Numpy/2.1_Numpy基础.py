import numpy as np
import random


# 创建数组的几种方法
# 将列表转化成为数组
t1 = np.array([1,2,3,4,5,6])
print(t1)
print(type(t1))
print("------------------------------")


t2 = np.array(range(10))
print(t2)
print(type(t2))
print("------------------------------")

# 用numpy生成一个数组
t3 = np.arange(10)
print(t3)
print(type(t3))
print("------------------------------")


t4 = np.arange(2,20,4)
print(t4)
print(type(t4))
print(t4.dtype)
print("------------------------------")

# 指定创建的数组的数据类型
t5 = np.array(range(1,4),dtype=float)
print(t5)
print(type(t5))
print(t5.dtype)
print("------------------------------")

# 修改数组的数据类型
t6 = t4.astype("int8")
print(t6)
print(t6.dtype)
print("------------------------------")

# 在numpy中生成小数
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)
print("------------------------------")

# numpy对小数的处理和修改
t8 = np.round(t7,2)
print(t8)
print(t8.dtype)
print("------------------------------")

# 数组的形状
t9 = np.arange(12)
print(t9)
print(t9.shape)
print("------------------------------")

t10 = np.array([[1,2,3],[4,5,6]])
print(t10)
print(t10.shape)
print("------------------------------")

t11 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(t11)
print(t11.shape)
print("------------------------------")

t12 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t12)
print(t12.shape)
print("------------------------------")

# 修改数组的形状
t13 = np.arange(12)
print(t13)
t14 = t13.reshape((3,4))
print(t14)
print("------------------------------")

t15 = np.arange(24).reshape((2,3,4))
print(t15)
# 将多维数组展开成为一维数组
print(t15.flatten())
print("------------------------------")

# 数组加数字
t16 = t15+2
print(t16)
print("------------------------------")

# 数组间的相加
t17 = t15 + t16
print(t17)
print("------------------------------")

# 不同行但同列的数组的相减，不同列但同行的数组同理
t18 = np.arange(2,10,2)
t19 = t17 -t18
print(t19)

# 广播原则：如果两个数组的后缘维度（即从末尾开始算起的维度）的轴长长相符或其中一方的长度为1，则认为它们是广播兼容的。广播会在缺失和（或）长度为1 的维度上进行。