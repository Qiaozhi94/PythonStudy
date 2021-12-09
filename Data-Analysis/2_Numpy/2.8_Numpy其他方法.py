import numpy as np
np.set_printoptions(suppress=True)  # 解决ndarray默认使用科学计数法显示的问题

test = np.arange(10,100,2).reshape((5,9))
print(test)
print("-"*100)

# 获取最大值和最小值的位置
a = np.argmax(test,axis=1)
b = np.argmin(test,axis=0)
print(b)
print(a)
print("-"*100)

# 创建一个全为0的数组
c = np.zeros((3,4),dtype=int)
d = np.ones((5,6),dtype=int)
print(c)
print(d)
print("-"*100)

# 创建一个对角线为1的正方形数组（方阵）
e = np.eye((10),dtype=int)
print(e)
print("-"*100)

# numpy生成随机数
f = np.random.randint(5,100,(4,5))  # 从给定的上下范围内选取随机数整数组成数组，范围为low，high，形状为shape
g = np.random.rand(1,3,2,5)   # 创建d0-dn维度的均匀分布的随机数数组，浮点数，范围为0-1
h = np.random.randn(1,3,2,5)  # 创建d0-dn维度的标准正态分布随机数，书店数，平均数0，标准差1
i = np.random.uniform(15,30,(4,5))   # 产生具有均匀分布的数组，low起始值，high结束值，size为形状
np.random.seed(5)  # 随机数种子，s是给定的种子值。因为计算机生成的是伪随机数，所以通过设定相同的随机数种子，可以每次生成相同的随机数
j = np.random.randint(10,100,(6,7))
k = np.random.randint(10,100,(6,7))
print(f)
print("-"*100)
print(g)
print("-"*100)
print(h)
print("-"*100)
print(i)
print("-"*100)
print(j)
print("-"*100)
print(k)
print("-"*100)

# numpy中的copy和view
l = np.random.randint(34,78,(4,5))
m = l   # 浅拷贝，l和m数组完全不复制，之间互相影响
l = np.arange(10,50).reshape(5,8)
print(l)
print(m)
print("-"*100)

n = np.random.randint(34,78,(4,5))
o = n[:]   # 视图的操作，是一种切片，会创造新的对象o，但是o的数据完全由n来保管，他们两个数组的数据变化是一致的
n = np.arange(10,50).reshape(5,8)
print(n)
print(o)
print("-"*100)

p = np.random.randint(34,78,(4,5))
q = p.copy()  # 复制，p和q之间互不影响
p = np.arange(10,50).reshape(5,8)
print(p)
print(q)
print("-"*100)

