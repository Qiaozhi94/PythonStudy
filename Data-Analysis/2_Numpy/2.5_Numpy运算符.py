import numpy as np

a1 = np.arange(0,30).reshape(6,5)
a2 = np.arange(0,30).reshape(6,5)
print(a1)
print("-"*100)

# 三元运算符
a3 = np.where(a1<10,0,10)
print(a3)
print("-"*100)

# 将a中小于10的数字替换成0，将大于20的数字替换成20
a4 = a2.clip(10,20)
print(a4)
print("-"*100)

# 将数组中的值修改成为nan
a5 = a4.astype(float)
# 因为nan是float格式的，所以需要先把一个int类型的整数转换成为一个float类型的浮点数
a5[4,4]=np.nan
print(a5)
print("-"*100)

