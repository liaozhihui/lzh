from multiprocessing import Process
import os
filename='./pic.jpg'

#获取文件大小
size=os.path.getsize(filename=filename)
#复制上半部分
def top():
    f=open(filename,'rb')
    n=size//2
    fw=open("half_top.jpg",'wb')
    while True:
        if n<1024:
            data=f.read(n)
            fw.write(data)
            break
        data=f.read(1024)
        fw.write(data)
        n -=1024
    f.close()
    fw.close()

def foot():
    f=open(filename,'rb')
    fw=open('half_bottom.jpg','wb')

    f.seek(size//2)

    while True:
        data=f.read(1024)
        if not data:
            break

        fw.write(data)
    f.close()
    fw.close()
t=Process(target=top)
f=Process(target=foot)

t.start()
f.start()
t.join()
f.join()
