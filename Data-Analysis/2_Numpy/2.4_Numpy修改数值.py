import numpy as np
np.set_printoptions(suppress=True)  # 解决ndarray默认使用科学计数法显示的问题

a1 = np.arange(0,24)
print(a1)
print("-"*100)



a2 = a1.reshape(4,6)
print(a2)
print("-"*100)

# Numpy中的布尔索引
print(a2 >10)

print("-"*100)

print(a2[a2<10])
print("-"*100)

a2[a2>10]=0
print(a2)