from matplotlib import pyplot as plt

fig = plt.figure(figsize=(20,15),dpi=100)



x = range(2,26,2)

y = [15,13,14,5,17,20,25,28,26,37,30,28]

plt.plot(x,y)

# 设置x轴的刻度
plt.xticks(x)
plt.yticks(range(min(y),max(y)+3))
# plt.yticks(y)



# plt.savefig("./1.png")
plt.show()
