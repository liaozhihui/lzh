from socket import *
import sys
import time
#全局变量
ADDR=(('127.0.0.1',8888))

#具体功能
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd=sockfd

    def do_list(self):
        self.sockfd.send(b'L') #发送请求
        #等待回复
        data=self.sockfd.recv(128).decode()

        if data=='OK':
            data=self.sockfd.recv(4096).decode()
            files = data.split(',')
            for file in files:
                print(file)

        else:
            #无法完成操作
            print(data)
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

    def do_get(self,filename):
        self.sockfd.send("G "+filename).encode()
        data=self.sockfd.recv(128).decode()
        if data =='OK':
            fd=open(filename,'wb')
            while True:
                data=self.sockfd.recv(1024)
                if data == b"##":
                    break
                fd.write(data)
            fd.close()
        else:
            print(data)

    def do_put(self,filename):

        try:
            f =open(filename,'rb')
        except IOError:
            print("没有该文件")
            return
        filename=filename.split('/')[-1]
        self.sockfd.send("P "+filename).encode()
        data=self.sockfd.recv(128).decode()

        if data == "OK":

            while True:
                data=f.read(1024)
                if not data:
                    time.sleep(0.1)
                    f.close()
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)


#网络链接
def main():
    #创建套接字
    sockfd=socket(AF_INET,SOCK_STREAM)


    #建立连接


    try:
        sockfd.connect(ADDR)

    except Exception as e:

        print("连接服务器失败：",e)
        return
    #创建文件处理类对象
    ftp=FtpClient(sockfd)


    while True:
        print("\n==============命令选项================")
        print("***      list        ***")
        print("***      get file    ***")
        print("***      put file    ***")
        print("***      quit    ***")

        cmd = input("输入命令>>")

        if cmd.strip() == "list":
            ftp.do_list()
        elif cmd[:3] == 'get':
            filename=cmd.strip().split()[-1]
            ftp.do_get()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'put':
            filename = cmd.strip().split()[-1]
            ftp.do_put(filename)
        else:
            print("请输入正确命令")

if __name__=="__main__":
    main()
