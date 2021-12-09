

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
    pass

M1 = Man("george",26)

M1.eat()
M1.sleep()


