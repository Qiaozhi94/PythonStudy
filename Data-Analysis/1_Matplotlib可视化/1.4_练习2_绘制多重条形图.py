# 假设你知道了列表a中电影分别在2017.09.14（b_14),2017.09.15(b_15),2017.09.16(b_16)三天的票房，为了展示列表中电影本身的票房以及同其他电影的数据对比情况，应该如何更加直观的呈现该数据：
from matplotlib import pyplot as plt
from matplotlib import font_manager

a = ['猩球崛起3：终极之战','敦刻尔克','蜘蛛侠：英雄归来','战狼2']
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

my_font = font_manager.FontProperties(fname="/Users/georgel./Library/Fonts/仿宋_GB2312.ttf")



plt.figure(figsize=(20,15),dpi=150)
plt.grid(alpha=0.2,linestyle="--")

bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]


plt.bar(range(len(a)),b_14,width=bar_width,label="2017.09.14")
plt.bar(x_15,b_15,width=bar_width,label="2017.09.15")
plt.bar(x_16,b_16,width=bar_width,label="2017.09.16")



plt.xticks(x_15,a,fontproperties=my_font,rotation=0,fontsize=20)
plt.legend(prop=my_font,loc=0)


plt.show()