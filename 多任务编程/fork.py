import os
from time import sleep
import sys
print(sys.version)

pid=os.fork()


if pid<0:

    print('Create process failed')

elif pid==0:
    sleep(2)
    print("The new process")
else:
    sleep(3)
    print("The old process")
print("fork test over")
