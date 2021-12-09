### **Scrapy框架：**

##### **Scrapy介绍**

**不是一个函数功能库，而是一个爬虫的框架**

爬虫框架：爬虫框架是实现爬虫功能的一个软件结构和功能组件集合。

爬虫框架是一个半成品，能够帮助用户实现专业网络爬虫。

##### **Scrapy爬虫框架结构：'5+2'结构**

包含Engine, Scheduler, Item Pipelines, Spiders, Downloader以及两个Middleware中间键模块。

###### **Engine模块：**

- 控制所有的模块之间的数据流
- 根据条件触发时间
- 不需要用户修改

###### **Downloader模块：**

- 根据请求下载网页
- 不需要用户修改

###### **Scheduler模块：**

- 对所有爬取请求进行调度管理
- 不需要用户修改

###### **Downloader Middleware中间键：**

目的：实现Engine, Scheduler和Downloader之间进行用户可配置的控制

功能：修改，丢弃以及新增请求或响应

用户可以编写配置代码

###### **Spider模块：**

- 解析Downloader返回的响应（Response）
- 产生爬取项（scraped item）
- 产生额外的爬取请求（Request）

###### **Item Pipeilines模块：**

- 以流水线方式处理Spider产生的爬取项
- 由一组操作顺序组成，类似流水线，每一个操作是一个Item Pipelines类型
- 可能操作：清理、检验和查重爬取项中的HTML数据，将数据存储到数据库中

用户自行编写配置代码

###### **Spider Middleware中间键：**

目的：对请求和爬取项的在处理

功能：修改，丢弃，新增请求或爬取项

用户可以自行编写配置代码

##### **Scrapy和requests库的比较**

相同点：

- 两者都可以进行页面请求和爬取，Python爬虫的两个重要技术路线
- 两者可用性都好，文档丰富，入门简单
- 两者都没有处理js，提交表单，应对验证码等功能（可拓展）

差异点：

|        Requests库        |         Scrapy框架         |
| :----------------------: | :------------------------: |
|        页面级爬虫        |         网站级爬虫         |
|          功能库          |            框架            |
| 并发性考虑不足，性能较差 |     并发性好，性能较高     |
|     重点在于页面下载     |      重点在于爬虫结构      |
|         定制灵活         | 一般定制灵活，深度定制困难 |
|       上手十分简单       |          入门较难          |

---

### **Scrapy命令行**

含义：Scrapy是为持续运行设计的专业爬虫框架，提供操作的Scrapy命令行

##### 格式：

~~~shell
>scrapy<command>[options][args]   #Scrapy命令在command位置体现
~~~

##### 常用命令：

|     命令     |          说明          |                   格式                   |
| :----------: | :--------------------: | :--------------------------------------: |
| startproject | 创建一个新工程（常用） |      scrapy startproject<name>[dir]      |
|  genspider   |  创建一个爬虫（常用）  | scrapy genspider [options]<name><domain> |
|   Settings   |    获得爬虫配置信息    |        scrapy settings [options]         |
|    crawl     |  运行一个爬虫（常用）  |           scrapy crawl<spider>           |
|     list     |  列出工程中所有的爬虫  |               scrapy list                |
|    Shell     |   启动URL调试命令行    |            scrapy shell [url]            |

##### 命令行逻辑：

- 命令行（不是图形界面）更容易自动化，适合脚本控制
- 本质上，Scrapy框架是给程序员使用的，功能（而不是界面）更重要

---

### **Scrapy产生步骤**

1. 建立一个Scrapy爬虫工程：

~~~shell
Scrapy startproject scrapy_demo
# 生成文件结构：
# scrapy_demo/            外层目录
    # scrapy.cfg          部署Scrapy爬虫的配置文件
    # scrapy_demo/        Scrapy框架的用户自定义Python代码
       # __int__.py       初始化脚本
       # items.py         Items代码模板（继承类）
       # middleware.py    Middleware代码模板（继承类）
       # pipelines.py     PipelineP代码模板（继承类）
       # setting.py       Scrapy爬虫的配置文件
       # spider/          Spiders代码模板目录（继承类）
          # __int__.py    初始文件，无需修改
          # __pycache__/  缓存目录，无需修改
~~~

2. 在工程中产生一个Scrapy爬虫

~~~shell
scrapy genspider demo python123.io    # scrapy genspider 爬虫名称 要爬取的网站
~~~

3. 配置产生的spider爬虫

4. 运行爬虫，获取网页

---

### **yield关键字**

yield 是一个生成器：

- 生成器是一个不断产生值的函数
- 包含yield语句的函数就是一个生成器
- 生成器每次产生一个值（yield语句），函数被冻结，被唤醒后在产生一个值

生成器写法：

~~~shell
def gen(n):    #yield写法
  for i in range(n):
    yield i**2
        
for i in gen(5):
  print(i,"",end="")
  
#输出结果是0 1 4 9 16
~~~

~~~shell
def square(n):   #普通写法
  ls = [i**2 for i in range(n)]
  return ls

for i in range(5):
  print(i,"",end="")
~~~

为什么需要生成器：

生成器相比于一次性列出所有内容的优势：

- 更节省存储空间
- 响应更迅速
- 使用更加灵活

---

### **Scrapy爬虫的使用步骤**

1. 创建一个工程和spider模板
2. 编写spider
3. 编写item pipeline
4. 优化配置策略

### **Scrapy爬虫的数据类型：**

- Request类：class scrapy.http.request()

1. Request对象表示一个http请求

2. 由spider生成，由Downloader执行

| 属性或方法 |                        说明                        |
| :--------: | :------------------------------------------------: |
|    .url    |                Request对象的URL地址                |
|  .method   |           对应的请求方法，'GET' 'POST'等           |
|  .headers  |                字典类型风格的请求头                |
|   .body    |              请求内容主体，字符串类型              |
|   .meta    | 用户添加的扩展信息，在Scrapy内部模板间传递信息使用 |
|  .copy()   |                     复制该请求                     |

- Response类

1. response对象表示一个HTTP响应
2. 由Downloader生成，由spider处理

| 属性或方法 |                说明                |
| :--------: | :--------------------------------: |
|    .url    |       response对象的URL地址        |
|  .status   |       HTTP状态码，默认是200        |
|  .headers  |       response对应的头部信息       |
|   .body    | response对象的内容信息，字符串类型 |
|   .flags   |              一组标记              |
|  .request  | 产生response类型对应的Request对象  |
|  .copy()   |             复制该响应             |

- Item类

Class scrapy.item.Item()

- Item对象表示一个从HTML页面中提取的信息内容
- 由Spider生成，由ItemPipeline处理
- ITem类似字典类型，可以按照字典类型操作

---

### **Scrapy爬虫提取信息的方法**

Scrapy爬虫支持多种HTML信息提取方法，主要在Sipder模块下：

- Beautiful Soup
- lxml
- re
- XPath Selector
- CSS Selector

---

### **CSS Selector**

CSS Selector由W3C组织维护并规范

~~~python
<HTML>.css('a::attr(href)').extract()
# a     标签名称
# href  标签属性
~~~











