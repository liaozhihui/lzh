
#coding:utf-8
import os

class Singleton(object):
  def __new__(cls,*args,**kwargs):
    if not hasattr(cls,'_inst'):
      cls._inst=super(Singleton,cls).__new__(cls,*args,**kwargs)
    return cls._inst
class A(Singleton):
        def __init__(self,s):
            self.s=s


li=[1,2,3,4]
a=A(li)

pid=os.fork()
if pid == 0:
        a.li.append(5)
        print("子进程的a",a.li)

elif pid > 0:
        print(a.li)
        os.wait()

