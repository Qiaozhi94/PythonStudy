

import time

def timer(func):  #func = test1
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func running time is %s" %(stop_time-start_time))
    return deco

@timer   #test1 = timer(test1)   #相当于给test1赋一个timer(test1)的内存地址
def test1():
    time.sleep(2)
    print("in the test1")

test1()

