import os 
from time import sleep 

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    sleep(3)
    print("The new process")
else:
    sleep(2)
    print("The old process")

print("fork test over")