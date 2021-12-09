import json
# 将python对象转换成json字符串
persons = [
    {
        'username':'alex',
        'age':'20',
        'country':'us'
    },{
        'username':'乔智',
        'age':'26',
        'country':'china'
    },{
        'username':'peter',
        'age':'50',
        'country':'uk'
    }
]

json_str = json.dumps(persons)
print(type(json_str))
print(json_str)
# <----------分隔符-------------->

# 将json数据直接存储到文件中
# json模块除了dumps函数之外还有一个dump函数，这个函数可以传入一个文件指针，直接将字符串dump到文件中

with open ('3.1.1_persons.json','w',encoding='utf-8') as fp:
    # fp.write(json_str)
    json.dump(persons,fp,ensure_ascii=False)

# 因为json在dump的时候，只能存放ASCII格式的字符，因此会对中文进行转义，这时候需要使用ensure_ascii=False指令关闭这个特性
# 在python中，只有基本数据类型才能转换成json格式的字符串，即：int, float, str, list, dict, tuple。