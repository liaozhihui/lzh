# coding=utf-8
import socket

socketfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketfd.connect(("127.0.0.1",8888))
while True:
    data=input(">>")
    if not data:
        break
    socketfd.send(data.encode())
    print(socketfd.recv(1024).decode())
socketfd.close()