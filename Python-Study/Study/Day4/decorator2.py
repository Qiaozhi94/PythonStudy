




import time


def test1():
    time.sleep(2)
    print("in the test1")




def deco(func):
    start_time = time.time()
    return func
    stop_time = time.time()
    print("the func's running time is %s" %(stop_time-start_time))




test1=deco(test1)

test1()

#deco(test1)