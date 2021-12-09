#Python支持多继承，但典型的Java就是不支持的


class People():
    def __init__(self,name,age):    #实例化
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..."% self.name)

    def sleep(self):
        print("%s is sleeping..."% self.name)

    def talk(self):
        print("&s is talking..."% self.name)

class Makefriends():
    def make_friends(self,obj):
        print("%s is making frineds with %s" %(self.name,obj.name))


class Man(People,Makefriends):
    def __init__(self,name,age,money):
        #People.__init__(self,name,age)
        super(Man, self).__init__(name,age)   #新式类写法  #这一句的作用个上面一句的作用完全相同，但是这一句更简洁
        self.money = money             #在子类中添加
        print("%s一出生就有%s块钱" % (name,money))

class Woman(People,Makefriends):
    def get_birth(self):
        print("a body is born by %s" % self.name)



M1 = Man("george",26,100)
W1 = Woman("lingzi",24)

M1.eat()
M1.sleep()
M1.make_friends(W1)

