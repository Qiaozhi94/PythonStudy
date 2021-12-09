class A:
    def __init__(self):
        print("A")
class B(A):
    pass
    def __init__(self):
        print("B")
class C(A):
    pass
    def __init__(self):
        print("C")
class D(B,C):
    pass
    def __init__(self):
        print("D")


obj = D()   #如果D中有构造函数的话，则优先执行D中的构造函数
            #这里如果D里没有构造函数的话，就优先走B的构造函数。
            #如果B没有的话，就优先走C的构造函数。
            #如果C也没有的话，就会选择走A的构造函数
            #这种查询策略就是广度优先原则，即先在横向尺度内从左到右依次检查
            #另外一种查询策略是深度优先原则，即一步一步沿着支线向上溯源，如果源头类也没有，则回来重新换一个子类继续溯源查询。
            #Python2经典类是按照深度优先来继承的，新式类是按照广度优先来继承的。
            #Python3经典类和新式类都是统一按照广度优先来继承的。