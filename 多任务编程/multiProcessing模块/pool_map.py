from multiprocessing import Pool
from time import sleep

def fun(n):
    sleep(1)
    return n*n

pool=Pool()

#使用map讲事件放入进程事件

r=pool.map(fun,[1,2,3,4,5])
pool.close()
pool.join()

print("结果：",r)