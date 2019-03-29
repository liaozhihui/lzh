from multiprocessing import Pool
from time import sleep, ctime


# 进程事件
def worker(msg):
    sleep(2)
    print(msg)


    #创建进程池
pool=Pool(4)

#向进程池添加事件
for i in range(10):
    msg="hello %d"%i
    pool.apply_async(func=worker,args=(msg,))

#关闭进程池
pool.close()

#回收进程池
pool.join()
