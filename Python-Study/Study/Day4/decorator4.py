

import time

def timer(func):  #func = test1
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("the func running time is %s" %(stop_time-start_time))
    return deco

@timer   #test1 = timer(test1)   #相当于给test1赋一个timer(test1)的内存地址
def test1():
    time.sleep(2)
    print("in the test1")

@timer       #test2 = timer(test2)   = deco   ,   test2()=deco()
def test2(name,age):
    print("test2:",name,age)



test1()
test2("alex",25)
