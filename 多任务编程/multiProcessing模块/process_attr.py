from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(3):
        sleep(2)
        print(ctime())
p=Process(target=tm,name="Tedu")

p.daemon=True
p.start()
print("alive2",p.is_alive())

print("Process name:",p.name)
print("Process PID",p.pid)
p.join(2)
print("==================")