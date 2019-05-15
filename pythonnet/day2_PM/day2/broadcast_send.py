from socket import *
from time import sleep 

#目标地址
dest = ('172.40.91.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data = '''
    ********************
      2.14 北京 雪
      往后余生，风雪是你
    ********************
'''

while True:
    sleep(2)
    s.sendto(data.encode(),dest)

s.close()