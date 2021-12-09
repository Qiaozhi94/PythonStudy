# 绘制随机列表模拟一天中的温度变化

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# windows和linux修改字体的方式
# font = {'family' : 'Microsoft YaHei',
#         'weight' : 'bold',
#         'size'   : 'larger'}
#
# matplotlib.rc("font",**font)
# matplotlib.rc("font",family="Microsoft YaHei",weight = "blod")


# 另一种设置字体的方式
my_font = font_manager.FontProperties(fname="/Users/georgel./Library/Fonts/仿宋_GB2312.ttf")




x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,10),dpi=100)

plt.plot(x,y)

# 调整x轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60,120)]

# 取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)

# 添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度（摄氏度）",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)


plt.show()