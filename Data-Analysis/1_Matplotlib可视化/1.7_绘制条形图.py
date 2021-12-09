# 在美国2004年人口普查发现有124million的人在离家相对较远的地方工作。根据他们从家到上班所需要的时间，通过抽样统计（最后一列）得出了下表的数据，这些数据可以绘制成直方图吗？

from matplotlib import pyplot as plt
from matplotlib import font_manager


interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

# for i in range(0,13):
#     a = quantity[i]
#     print(a)

plt.figure(figsize=(20,15),dpi=150)

plt.bar(range(len(quantity)),quantity,width=1,edgecolor='black')

_x = [i-0.5 for i in range(13)]
_xticks_labels = interval + [150]


plt.xticks(_x,_xticks_labels)
# plt.yticks(range(min(quantity),max(quantity)+1000,500))
# plt.yticks(range(0,13),quantity)

# 设置数字标签 这里运行报错，不知道是何原因
for a,b in zip(interval,quantity):
    plt.text(interval,quantity,'%3f' %b, ha="center",va="bottom",fontsize=10)

plt.grid(alpha=0.3,linestyle="--")
plt.show()

