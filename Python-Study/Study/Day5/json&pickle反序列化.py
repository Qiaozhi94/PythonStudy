#import json
import pickle



f = open("test.text", "rb")
#data = json.loads(f.read())
data = pickle.loads(f.read())

print(data["age"])