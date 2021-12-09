# 电影票房排行榜的竖向条形统计图
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np

my_font = font_manager.FontProperties(fname="/Users/georgel./Library/Fonts/仿宋_GB2312.ttf")

a = ['战狼2', '哪吒之魔童降世', '流浪地球', '复仇者联盟4：终局之战', '红海行动', '美人鱼', '唐人街探案2', '我和我的祖国', '我不是药神', '中国机长', '速度与激情8', '西虹市首富', '速度与激情7', '捉妖记', '复仇者联盟3：无限战争', '捉妖记2', '羞羞的铁拳', '疯狂的外星人', '海王', '变形金刚4：绝迹重生']
b = [56.39, 49.34, 46.18, 42.05, 36.22, 33.9, 33.71, 31.46, 30.75, 28.84, 26.49, 25.27,24.26, 24.21, 23.7, 22.19, 21.9, 21.83, 19.97, 19.79]



c = int(min(b))
d = int(max(b))

plt.figure(figsize=(20,15),dpi=100)
plt.grid(alpha=0.2)
plt.barh(range(len(a)),b)
plt.yticks(range(len(a)),a,fontproperties=my_font,rotation=360,fontsize=12)
plt.xticks(range(0,d+5),fontproperties=my_font,fontsize=12)
plt.show()