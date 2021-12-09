class People():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..."% self.name)

    def sleep(self):
        print("%s is sleeping..."% self.name)

    def talk(self):
        print("&s is talking..."% self.name)

class Man(People):
    def __init__(self,name,age,money):
        #People.__init__(self,name,age)
        super(Man, self).__init__(name,age)   #这一句的作用个上面一句的作用完全相同，但是这一句更简洁
        self.money = money             #在子类中添加
        print("%s一出生就有%s块钱" % (name,money))

M1 = Man("george",26,100)

M1.eat()
M1.sleep()


