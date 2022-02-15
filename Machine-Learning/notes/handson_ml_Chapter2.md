# **性能选择指标**
回归问题的典型性能选择指标是**均方根误差（RMSE）**，它表示预测值和观测值之间差异（称为残差）的样本标准差。做非线性拟合时,RMSE越小越好。
#### 均方根误差（RMSE）公式：
$$\operatorname{RMSE}(\boldsymbol{X}, h)=\sqrt{\frac{1}{m} \sum_{i=1}^{m}\left(h\left(\boldsymbol{x}^{(i)}\right)-y^{(i)}\right)^{2}}$$
其中：
* $m$ 是要在其上测量RMSE的数据集中的实例数，即训练样本数
* $x^{(i)}$ 是数据集中第i个实例的所有特征值（不含标签）的向量，而$y^{(i)}$是其标签（该实例的期望输出值）。例如第一个区域位于经度-118.29°，纬度33.91°，居民1416人，收入中位数为38372美元，房屋价值中位数为156400美元（忽略其他特征），那么：
$$\boldsymbol{x}^{(1)}=\left(\begin{array}{c}
-118.29 \\
33.91 \\
1416 \\
38372
\end{array}\right)$$
$$y^{(1)}=156400$$
* $x$ 是一个矩阵，其中包含数据集中所有实例的所有特征值（不包括标签）。每个实例只有一行，第 $i$ 行等于 $x^{(i)}$ 的转置，记为 $\left(x^{(i)}\right)^{T}$ 。例如，如果第一个区域数据如上，则矩阵 $X$ 如下：
$$\boldsymbol{X}=\left(\begin{array}{c}
\left(\boldsymbol{x}^{(1)}\right)^{\mathrm{T}} \\
\left(\boldsymbol{x}^{(2)}\right)^{\mathrm{T}} \\
\vdots \\
\left(\boldsymbol{x}^{(1999)}\right)^{\mathrm{T}} \\
\left(\boldsymbol{x}^{(2000)}\right)^{\mathrm{T}}
\end{array}\right)=\left(\begin{array}{cccc}
-118.29 & 33.91 & 1416 & 38372 \\
\vdots & \vdots & \vdots & \vdots
\end{array}\right)$$
* $h$ 是系统的预测函数，也称为假设。当给系统输入一个实例的特征向量 $x^{(i)}$ 时，他会为该实例输出一个预测值 $\hat{y}^{(i)}=h\left(\boldsymbol{x}^{(i)}\right)$。例如如果系统预测第一个区域的房价中位数为158400美元，则 $\hat{y}^{(i)}=h\left(\boldsymbol{x}^{(i)}\right)=158400$ 。该区域的预测误差为 $\hat{y}^{(1)}-y^{(1)}=2000$。
* $\operatorname{RMSE}(X, h)$ 时使用假设 $h$ 在一组实例中测量的成本函数。
**注明**：小写斜体字体表示标量值（如 $m$ 和 $y^{(i)}$ )和函数名称 $h$ ，将小写粗斜体字体用于向量（如 $\boldsymbol{x}^{(i)}$ ），将大学粗体字体用于表示矩阵（如 $\boldsymbol{X}$ ）
---
**平均绝对误差（MAE）** 也称为绝对平均偏差，同样也是衡量回归任务中的重要性能指标，它表示预测值和观测值之间绝对误差的平均值。
#### 平均绝对误差（MAE）：
$$\operatorname{MAE}(\boldsymbol{X}, h)=\frac{1}{m} \sum_{i=1}^{m}\left|h\left(\boldsymbol{x}^{(i)}\right)-y^{(i)}\right|$$
均方根误差（RMSE）和平均绝对误差（MAE）都是测量两个向量（预测值向量和目标值向量）之间距离的方法。其中他们有如下区别：
* 均方根误差（RMSE）是计算平方和的根与欧几里得范数相对应：这是计算距离的概念，它也称为 $\ell_{2}$ 范数，记作 $\| \cdot||_{2}$ 或 $\| \cdot||$ 。
* 平均绝对误差（MAE）是计算绝对值之和，对应于 $\ell_{1}$ 范数，记作 $\| \cdot||_{1}$ 。有时将其称为曼哈顿范数。
* 一般而言，包含n个元素的向量 $V$ 的 $\ell_{k}$ 范数定义为 $\|\boldsymbol{v}\|_{k}=\left(\left|v_{0}\right|^{k}+\left|v_{1}\right|^{k}+\cdots+\left|v_{n}\right|^{k}\right)^{1 / k}$ 。$\ell_{0}$ 给出了向量中的非零元素数量，$\ell_{\infty}$ 给出了向量中的最大绝对值。
* MAE是一种线性分数，所有个体差异在平均值上的权重都相等，比如，10和0之间的绝对误差是5和0之间绝对误差的两倍。但这对于RMSE而言不一样，后续的例子将进一步详细讨论。MAE很容易理解，因为它就是对残差直接计算平均，而RMSE相比MAE，会对高的差异惩罚更多。
---
#### 具体例子
案例1：真实值= [2,4,6,8]，预测值= [4,6,8,10]  
案例2：真实值= [2,4,6,8]，预测值= [4,6,8,12]  
案例1的MAE = 2.0，RMSE = 2.0 
案例2的MAE = 2.5，RMSE = 2.65
从上述例子中，我们可以发现RMSE比MAE更加多地惩罚了最后一项预测值。通常，RMSE要大于或等于MAE。等于MAE的唯一情况是所有残差都**相等或都为零**，如案例1中所有的预测值与真实值之间的残差皆为2，那么MAE和RMSE值就相等。

---
# 机器学习通用流程

**1. 安装CUDA和Tensorflow, Sk-learning**
按照网上通用教程进行安装，一般问题不多。
需要注意的是：
	* 在本机NVIDIA控制面板下查看nvcuda.dll的属性时是cuda 11.6.99驱动，但是官网下载11.6的版本一直安装不上，安装11.5却可以安装成功，这里建议安装11.5的版本，尽量避免出现一些疑难杂症。
	* 安装tensorflow成功之后，在conda命令界面强烈建议使用pip进行包管理，之前博主使用conda install命令安装matplotlib时，出现了依赖的包的版本要求不一致的情况导致matplotlib一直安装不上，后使用pip一次即正确安装好可以使用。

**2. 配置机器学习虚拟环境及所需要的依赖包**
书中本章采用Jupyter notebook来进行演示，好处是轻量且直观。但博主自己有rtx显卡的笔记本，所以正好借此机会安装cuda，所以就使用了pycharm的pro版本（学生免费）来进行实验。
配置环境的部分不在赘述，强烈建议使用anaconda3来管理，新建一个虚拟环境，在conda界面中使用pip安装必要的依赖包，然后在ide中自由切换虚拟环境，非常方便。
**3. 下载数据**
不同目的的机器学习的数据来源是不一样的，书中是写了一个函数自动从github网站上在相应目录下自动获取csv文件，这里博主整个fork了handson-ml2的这个仓库并且同步到了本地，所以就把要用到的csv文件复制到了python文件同目录下，从而省掉了下载数据的步骤。
**4. 检查数据结构**
数据集csv文件准备好之后，在着手开始后续步骤之前需要先检查数据结构，以防之后的学习与分析过程出现什么明显的问题。
```python
import pandas as pd  
import matplotlib.pyplot as plt  

hs = pd.read_csv('housing.csv')  
print(hs)  
print("----------------------------------------")  
print(hs.info())  # 打印出csv文件的全部属性  
# print(a.to_string())  # 打印出全部的csv数据  
print("----------------------------------------")  
print(hs["ocean_proximity"].value_counts())  # 查看csv文件中object的分类与数量关系  
print(hs.describe())  # 查看csv文件中的所有数据的摘要和大致分布  
print("----------------------------------------")  
hs.hist(bins=50, figsize=(20, 15))  
plt.show()  # 绘制各个指标分布图表进一步更准确的查看数据信息的分布
print("----------------------------------------")  
```

**5. 创建测试集**

在机器学习第一个阶段需要先创建测试集，以便之后机器学习完成后对学习成果进行测试。一般上创建测试集比较简单，只需要随机选择一些实例，通常是整个数据集的20%（如果数据量非常大，则比例可能会更小）
以下是创建数据集的第一阶段，分为分步熟悉阶段和完整代码阶段：
 ```python
 #!/usr/bin/env python3  
# _*_coding:utf-8_*_  
"""  
@ File    :2-2分离测试集-1.py  
@ Time    :2022/2/11  15:00  
@ Author  :qiaozhi94  
@ Email   :qiaozhi_li@126.ocm  
@ IDE     :PyCharm  
"""  
import pandas as pd  
import numpy as np  
  
# 分步熟悉阶段  
a = np.random.permutation(10)  # 输入一个数，结果是生成一个随机序列  
arr1 = np.arange(9).reshape((3, 3))  # 输入一个数组，结果是生成一个数组的随机序列  
b = np.random.permutation(arr1)  
print(a)  # 生成了一个随时序列  
print(arr1)  # 快速生成一个三维数组  
print(b)  # 和arr结果对比可知，permutation函数只对数组第一维进行打乱  
print("----------------------------------------")  
c = a[:3]  # 选取随机序列a中的前三个数字成为单独的数组  
d = a[5:]  # 选取随机序列a中的后五个数字成为单独的数组  
print(c)  
print(d)  
print("----------------------------------------")  
  
arr2 = pd.DataFrame(np.arange(16).reshape(4, 4), index=list('abcd'), columns=list('ABCD'))  
print(arr2)  
print(arr2.loc['a'])  # 取索引为'a'的行  
print(arr2.iloc[0])  # 取第一行数据，索引为'a'的行就是第一行，所以结果与上面的相同  
print(arr2.loc[:, ['A']])  # 取'A'列所有行，多取几列格式为 data.loc[:,['A','B']])print(arr2.iloc[:, [0]])  # 取第0列所有行，多取几列格式为 data.iloc[:,[0,1]])  
  
# 完整代码阶段  
def split_train_test(data, test_ratio):  
    shuffled_indices = np.random.permutation(len(data))  # 输入数据集的实例总数随机生成一个随机序列（见分步熟悉阶段）  
 test_set_size = int(len(data) * test_ratio)  # 输入比例后得出测试集的实例数  
 test_indices = shuffled_indices[:test_set_size]  # 按照测试集的大小选取随机虚列的前xx位数字标签  
 train_indices = shuffled_indices[test_set_size:]  # 选取出测试集之后剩下的数字标签所对应的数据即为训练集的数据  
 return data.iloc[train_indices], data.iloc[test_indices]  # 根据所选择的数字标签分别摘录出测试集与训练集的数据  
  
  
hs = pd.read_csv('housing.csv')  
train_set, test_set = split_train_test(hs, 0.2)  
print(train_set)  
print(len(train_set))  
print(test_set)  
print(len(test_set))
 ```

这样创建测试集会出现一个重大的问题，即每次运行都会是不一样的测试集，这样下去，机器就会陆续看到完整的数据集，这正是创建测试集的时候所要避免的。
简单的解决方案是第一次运行程序后直接保存测试集到csv文件中，之后的运行只是调用加载它即可。另一种方法是在调用np.random.permutation()函数之前先设置一个随机数生成器的种子，从而让它始终生成相同的随机索引。
但是，这两种解决方案在下一次获取更新的数据时都会中断。为了即使在更新数据集之后也有一个稳定的训练测试分割原则，常见的解决方案是每个实例都使用一个标识符来决定是否进入测试集（假定每个实例都有一个唯一且不变的标识符）。在这里在仔细观察数据集之后发现可以使用完全不变的区域的经纬度作为唯一且不变的标识符来进行分割数据集的工作。
以下为使用Scikit-Learn库中的train_test_split()函数来快速进行分割数据集操作的代码：
```python
#!/usr/bin/env python3  
# _*_coding:utf-8_*_  
"""  
@ File    :2-2分离测试集-随机抽样.py  
@ Time    :2022/2/14 16:18  
@ Author  :qiaozhi94  
@ Email   :qiaozhi_li@126.ocm  
@ IDE     :PyCharm  
"""  
  
# 2-2分离测试集-1.py文件中只是使用了最简单随机的生成方法来分离测试集，这里则采用Scikit-Learn包中的train_test_split（）函数，其与前面定义的  
# 函数split_train_test（）几乎相同，除了几个额外特征。首先，它也有random_state参数，让你可以设置随机生成器种子；  
# 其次，你可以把行数相同的多个数据集一次性发送给它，它会根据相同的索引将其拆分（例如，当你有一个单独的DataFrame用于标记时，这就非常有用）  
  
from sklearn.model_selection import train_test_split  
import pandas as pd  
  
hs = pd.read_csv('housing.csv')  
train_set, test_set = train_test_split(hs, test_size=0.2, random_state=50)  
  
print(train_set)  
print("-----------------------------------------------------------------------")  
print(test_set)  
  
# 这是纯随机的抽样方法，如果数据集足够庞大（特别是相较于属性的数量而言），这种方式通常不错；如果不是的话，则有可能会导致明显的抽样偏差。  
# 2-2分离测试集-分层抽样.py文件中则讲解了分层抽样方法，相比之下会更加准确。
```

以上都是纯随机的抽样方法，非常适用于数据量十分庞大且分布相对随机均匀的情况下。但大部分真实的数据都会存在不完全随机的情况，这时可以考察重要属性的分布情况来进行分层抽样得出测试集，可以更加准确的得知机器学习的成果。
在本案例中可以采取收入中位数作为重要属性均分为六组后按照每组所占的比例分割数据集，代码如下：
```python
#!/usr/bin/env python3  
# _*_coding:utf-8_*_  
"""  
@ File    :2-2分离测试集-分层抽样.py  
@ Time    :2022/2/14 16:56  
@ Author  :qiaozhi94  
@ Email   :qiaozhi_li@126.ocm  
@ IDE     :PyCharm  
"""  
  
# 本次尝试使用分层抽样方法替代随机抽样方法，这里采用收入中位数这一重要属性来衡量放家中位数。  
# 目标是希望确保在收入属性上，测试集能够代表整个数据集中各种不同类型的收入。  
  
  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import StratifiedShuffleSplit  
  
hs = pd.read_csv('housing.csv')  
hs["income_column"] = pd.cut(hs["median_income"], bins=[0., 1.5, 3.0, 4.5, 6., np.inf], labels=[1, 2, 3, 4, 5])  
# np.inf表示无穷大的意思  
hs["income_column"].hist()  
plt.show()  # 先将数据集的收入中位数按照从小到大的顺序均分为六组，然后绘图得到数据集在这六组中的分布  
  
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)  
# 接下来就可以通过StratifiedShuffleSplit函数进行分层抽样区分测试集和训练集了  
  
for train_index, test_index in split.split(hs, hs["income_column"]):  
    strat_train_set = hs.loc[train_index]  
    strat_test_set = hs.loc[test_index]  
print(strat_test_set)  
print("-----------------------------------------------------------------------")  
print(strat_train_set)
```

**6. 数据可视化&寻找相关性**

之前的检查数据只是粗略的观察数据的结构，现在我们需要知道房价中位数与哪些指标或属性具有强相关性，第一步我们需要将数据集可视化来更加深入的观察数据，所以根据经纬度数据绘制出数据集的散点图，同时设置alpha数值，可以更加清楚的查看散点图细节。最后设置圆的半径为人口数，圆的颜色表示房价中位数的高低，蓝色是低，红色是高，最后得出最终信息表达最明确的数据集散点图。
在充分查看完成可视化的数据之后，我们需要进一步得知房价中位数与哪些属性具有强相关性，可以使用pandas的相关性系数-DataFrame.corr()函数来计算出每对属性之
间的标准相关系数（也称为皮尔逊r）。
可以看到返回的矩阵数据得知：相关系数的范围从-1变化到1。越接近1，表示有越强的正相关。例如，当收入中位数上升时，房价中位数也趋于上升。当系数接近于-1时，表示有较强的负相关。我们可以看到纬度和房价中位数之间呈现出轻微的负相关（也就是说，越往北走，房价倾向于下降）。最后，系数靠近0则说明二者之间没有线性相关性。

```python
#!/usr/bin/env python3  
# _*_coding:utf-8_*_  
"""  
@ File    :2-4可视化训练集数据.py  
@ Time    :2022/2/15 12:11  
@ Author  :qiaozhi94  
@ Email   :qiaozhi_li@126.ocm  
@ IDE     :PyCharm  
"""  
  
import pandas as pd  
import matplotlib.pyplot as plt  
  
hs = pd.read_csv('housing_test.csv')  
hs.plot(kind="scatter", x="longitude", y="latitude")  # 根据经纬度画出数据集所分布的位置散点图  
hs.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)  # 修改alpha值，可以比较清楚的看到高密度数据点的位置  
hs.plot(kind="scatter", x="longitude", y="latitude", alpha=0.05)  
  
hs.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,  
 s=hs["population"] / 100, label="population", figsize=(10, 7),  
 c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True, )  
# 使用圆的半径表示人口的多少，圆的颜色表示房价的高低，此时调用一个叫jet的预设颜色表可以画出更加清晰的价格与人口关系的散点分布图  
  
plt.legend()  
plt.show()  
  
# 寻找数据相关性  
corr_matrix = hs.corr()  # 由于数据集不大，你可以使用corr（）方法轻松计算出每对属性之间的标准相关系数（也称为皮尔逊r）：  
print(corr_matrix["median_house_value"].sort_values(ascending=False))  
# 查看结果可以看出与median_house_value与各个属性之间的相关性系数分布于1到-1之间, 分别为正相关，不相关与负相关性关系  
# median_house_value    1.000000  
# median_income         0.688075  
# total_rooms           0.134153  
# housing_median_age    0.105623  
# households            0.065843  
# total_bedrooms        0.049686  
# population           -0.024650  
# longitude            -0.045967  
# latitude             -0.144160  
# Name: median_house_value, dtype: float64  
  
# 画出收入中位数与房价中位数的散点关系图  
hs.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.05)  
plt.show()
```


**7. 机器学习算法的数据准备**