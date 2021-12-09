data = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{"CICC","HP"},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '广东':{
        "东莞":{},
        "中山":{},
        "佛山":{"碧桂园"},
    },
}
exit_flag = False

while not exit_flag:
    for i in data:
        print(i)

    choice = input("选择进入1：")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("选择进入2：")
            if choice2 in data[choice]:
                while not exit_flag:
                  for i3 in data[choice][choice2]:
                    print("\t",i3)
                  choice3 = input ("选择进入3：")
