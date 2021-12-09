
import time

def bar():
    time.sleep(2)

    print("in the bar")

def test1(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print("running time: %s" %(stop_time-start_time))

test1(bar)


