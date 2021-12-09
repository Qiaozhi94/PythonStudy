#import json
import pickle



f = open("test.text", "rb")
#data = json.loads(f.read())

data = pickle.load(f)  #data = pickle.loads(f.read())  #这两句语法也完全一样
print(data["age"])