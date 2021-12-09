import json

json_str = '[{"username": "alex", "age": "20", "country": "us"}, {"username": "乔智", "age": "26", "country": "china"}, {"username": "peter", "age": "50", "country": "uk"}]'

persons = json.loads(json_str)
print(type(persons))
for person in persons:

    print(type(person))
    print(person)

# <--------------------分隔符---------------------->

# 如果想直接从文件中读取json字符串并转换成为python对象的话，如下：

with open('3.1.1_persons.json','r',encoding='utf-8') as fp:
    persons_1 = json.load(fp)
    print(type(persons_1))
    print(persons_1)
    for person_1 in persons_1:
        print(type(person_1))
        print(person_1)