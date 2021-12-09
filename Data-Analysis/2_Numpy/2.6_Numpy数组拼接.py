# 数组的拼接/分割/交换
import numpy as np
np.set_printoptions(suppress=True)  # 解决ndarray默认使用科学计数法显示的问题


a1 = np.arange(20,50).reshape(6,5)
a2 =np.arange(0,20).reshape(4,5)
a3 = np.arange(24).reshape(6,4)

# print(a1)
# print(a2)
# print(a3)

# 竖直拼接
b1 = np.vstack((a2,a1))
print(b1)
print("-"*100)

# 水平拼接
b2 = np.hstack((a1,a3))
print(b2)
print("-"*100)

# 行交换
a1[(2,1),:] = a1[(1,2),:]
print(a1)
print("-"*100)

# 列交换
a2[:,(3,4)] = a2[:,(4,3)]
print(a2)
print("-"*100)

print(a3.shape)
print("-"*100)

# 在数组旁边拼接一段全为0的数组
# 构造一列全为0的数据
c = np.zeros((a3.shape[0],1),dtype=int)
d = np.ones((a2.shape[0],1),dtype=int)
print(d)
print("-"*100)
print(c)
print("-"*100)
# 拼接两段数组
e = np.hstack((a3,c))
print(e)

