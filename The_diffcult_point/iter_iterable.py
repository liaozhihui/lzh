#coding:utf-8

#迭代器一定是迭代对象，反过来则不是，
#迭代对象是定义__iter__()方法，返回迭代器
#迭代器是定义了__iter__()和__next__()
#生成器是特殊的迭代器，yeild的作用和__iter__()和__next__()的作用相同
from collections import Iterable,Iterator
class Myrange(object):
    def __init__(self,start,end,step=1):
        self.start=start
        self.end=end
        self.step=step

    def __iter__(self):
        print("=")
        # return genetor()
        return IteratorRange(self.start,self.end,self.step)


class IteratorRange(object):
    def __init__(self,start,end,step=1):
        self.start=start
        self.end=end
        self.step=step

    def __iter__(self):
        print("=")
        return self

    def __next__(self):
        if self.start<self.end:
            self.start+=self.step
        else:
            raise StopIteration
        return self.start
if __name__=="__main__":
    for i in Myrange(0,10):
        print(i)
    print(isinstance(Myrange(0,1),Iterable))
    print(isinstance(IteratorRange(0,1), Iterator))