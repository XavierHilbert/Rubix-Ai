from threading import Thread
import time

def x(): 
    print(10)
    time.sleep(1)

thread = Thread(target = x)
thread.start()
print("hello")
thread.join()
print("world")