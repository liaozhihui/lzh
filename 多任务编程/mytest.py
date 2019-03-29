from multiprocessing import Process,Value
import os
import time


num=Value('i',1)

def addNum1():
    while True:
        num.value+=1
        # time.sleep(0.1)
        if num.value==1000:
            break

def addNum2():
    while True:
        num.value+=1
        # time.sleep(0.1)
        if num.value==1000:
            break

# def addNum3():
#     for i in range(10000):
#         num.value+=1
#
# def addNum4():
#     for i in range(10000):
#         num.value+=1


p1=Process(target=addNum1)
p2=Process(target=addNum2)
t1=time.time()
p1.start()
p2.start()
p1.join()
p2.join()
t2=time.time()

print("多进程",t2-t1)
print(num.value)




