# 假设大家在30岁的时候，根据自己的实际情况统计出来了从11岁到30岁每年搬家的次数如列表a，请绘制出该数据的折线图，以便分析自己每年搬家次数的走势和频率。
# a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
# y轴表示次数
# x轴表示岁数，比如11岁或12岁等

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/Users/georgel./Library/Fonts/mingliu.ttc")

plt.figure(figsize=(20,10),dpi=100)


x = range(11,31)
y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,2,3,2,0,1,5,4,3,3,1,2,1,1,1,1,1,1,1,1]



plt.plot(x,y_1, label="自己",color="grey",linestyle=":")
plt.plot(x,y_2, label="同桌",color="black",linestyle="--")

x_label = ["{}岁".format(i) for i in range(11,31)]
# print(type(x_label))

plt.xticks(list(x),x_label,fontproperties=my_font)

plt.xlabel("年龄（岁）",fontproperties=my_font)
plt.ylabel("次数（次）",fontproperties=my_font)
plt.title("11岁到30岁每年搬家次数的统计",fontproperties=my_font)

# 绘制网格
plt.grid(alpha=0.2,linestyle="--")
# 添加图例
plt.legend(prop=my_font,loc=0)

plt.show()

