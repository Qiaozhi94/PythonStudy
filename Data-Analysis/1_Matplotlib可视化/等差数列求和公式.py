
min_number = input("请输入最小整数字：")
max_number = input("请输入最大整数字：")
step = input("请输入整数间隔：")

if min_number.isdigit() and max_number.isdigit() and step.isdigit():
    if int(max_number) > int(min_number):
        a = []
        b = range(int(min_number), int(max_number) + 1, int(step))
        for i in b:
            a.append(i)
            # print(len(a))
            # print(a)
        if int(max_number) > max(a):
            a.append(int(max_number))
        else:
            pass
        print(a)

        c = (int(max_number) - int(min_number)) / int(step)
        if str(c).isdigit():
            e = (len(a)-1)/2
            d = (int(min_number) + int(max_number)) * e + a[e+1]
            print(d)
        else:
            e = (len(a)-1)/2
            d = (int(min_number) + a[-2]) * e + a[-1]
            print(d)
    else:
        print("最大整数需大于最小整数！")
else:

    print("请输入整数字！")




