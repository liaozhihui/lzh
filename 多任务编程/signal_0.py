import signal
import os

#处理子进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid=os.fork()

if pid<0:
    print("Error")
elif pid==0:
    print("Child PID:",os.getpid())
else:
    while True:
        pass