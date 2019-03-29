import threading

from time import sleep

import os

#线程函数

a=1

def music():
    global a
    print('a=',a)
    a=1000
    for i in range(5):
        sleep(2)
        print("播放学猫叫",os.getpid())

#创建线程对象

t=threading.Thread(target=music)
t.start()

#主线程运行任务
for i in range(3):
    sleep(3)
    print("燃烧我的卡路里",os.getpid())

t.join()

print("Main thread a",a)