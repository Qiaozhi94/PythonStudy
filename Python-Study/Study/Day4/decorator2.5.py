import time


def test1():
    time.sleep(2)
    print("in the test1")



def timer(func):

 def deco():
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func's running time is %s" %(stop_time-start_time))
 return deco

test1=timer(test1)
#print(timer(test1))   #内存地址

test1()
