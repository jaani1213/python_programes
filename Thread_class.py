import threading
from threading import *
from time import sleep

class First_thread(Thread):
    def run(self):
        for i in range(1,10):
            print(i,"this is 1st thread")
            #sleep(1) # 1 milli second

class Second_thread(Thread):
    def run(self):
        for i in range(1,10):
            print(i,"this is 2nd thread")
            #sleep(1)
            
            
t1=First_thread() # t1,t2 are objects
t2=Second_thread()                       
# t1.run()
# t2.run()

# t1.start()
# # sleep(1)
# print(t1.is_alive())
# t2.start()
# # sleep(1)
# print(t2.is_alive())

# t1.start()
# print(t1.is_alive())
# t2.start()
# print(t2.is_alive())
# t1.join()
# t2.join()
# print(t1.is_alive())
# print(t2.is_alive())


# import threading
# print(threading.current_thread().getName())