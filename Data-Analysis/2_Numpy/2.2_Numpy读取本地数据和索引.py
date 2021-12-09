import numpy as np


test1 = np.loadtxt("data.csv",delimiter=",",dtype="int",skiprows=1)
test2 = np.loadtxt("data.csv",delimiter=",",dtype="int",unpack=True,skiprows=1)
test3 = test1.transpose()

print(test1)
print("-"*100)

# 数组的转置
print(test2)
print("-"*100)
print(test3)

print("-"*100)
print(test1[2,3])


