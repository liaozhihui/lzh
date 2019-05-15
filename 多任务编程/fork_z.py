import os
from time import sleep

pid=os.fork()

if pid == 0:
    print("Child PID:",os.getpid())

else:
    print("Parent process,长点心吧")
    while True:
        pass