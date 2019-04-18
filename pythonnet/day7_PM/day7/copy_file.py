from multiprocessing import Process 
import os
from time import sleep

filename = "./test.jpg" 
#获取文件大小
size = os.path.getsize(filename)

# f = open(filename,'rb')

#复制上半部分
def top():
    # sleep(1)
    f = open(filename,'rb')
    n = size // 2 
    fw = open("half_top.jpg",'wb')
    # fw.write(f.read(n))
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break 
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()

#复制下半部分
def boot():
    f = open(filename,'rb')
    fw = open('half_bottom.jpg','wb')
    f.seek(size//2,0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()

t = Process(target=top)
b = Process(target=boot)
t.start()
b.start()
t.join()
b.join()


