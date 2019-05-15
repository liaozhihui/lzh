import os
from time import sleep


a=1
pid=os.fork()
print("******************")
if pid<0:
    print("create Process failed")
elif pid == 0:
    print("Child process")
    print("a = %d"%a)
    a=10000
else:
    sleep(1)
    print("Parent process")
    print("a:",a)

print("all a=",a)