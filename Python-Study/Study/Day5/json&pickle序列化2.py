#序列化和反序列化本质都是用于Python特有的类型（json只是字符串）和Python的数据类型之间进行转换的工具

#import json
import pickle #pickle和json的作用完全一样，只是json只能处理列表及字典等简单数据，但是好处是可以用于java和python的数据交互和传递


#def sayhi(name):
    #print("hello", name)   #json只能处理简单的数据类型，如字典和列表，不能处理函数。


info = {"name":"george","age":22,}
#info = {"name":"george","age":22,"func":sayhi}

f = open("test.text", "wb")
#f.write(json.dumps(info))

pickle.dump(info,f)  #f.write(pickle.dumps(info))  #两句语法完全一样
f.close()
print(f)