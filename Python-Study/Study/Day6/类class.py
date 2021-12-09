#类的初步应用和传参

class role():
    n = 123    #类变量，可作为初始默认的变量
    def __init__(self,name,role,weapon,life_value=100,money=10000):
        #构造函数  #作用是在实例化时做一些类的初始化工作，即
        self.name = name    #实例变量（静态属性），将变量赋值给了实例（区别于类变量），作用域是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        #print()

    def shot(self):    #类的方法，也就是功能（动态属性）
        print("%s just got shot..."%self.name)

    def buy_gun(self,gun_name):
        print("%s just bought %s"%(self.name,gun_name))

r1 = role("george","police","ak47")   #把抽象的类实例化&具体化（初始化一个类），相当于创造一个对象
r2 = role("alex","police","b51")
#print(r1)    #这一步打印出来是内存地址，不知道是为什么？
#print(r2)    #只能通过继续调用buy_gun的函数以及其内的print指令才能输出正确结果？

print(role.n)
r1.buy_gun("b51")
r2.shot()