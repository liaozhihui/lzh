import os
from time import sleep

pid=os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child %d process exit"%os.getpid())
    os._exit(2)
else:
    pid,status=os.wait()
    while True:
        pass