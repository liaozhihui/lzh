# coding=utf-8
class A(object):
    def hao(self):
        print("A")

class B(A):
    def hao(self):
        print(self.__class__.__mro__)
        super(B,self).hao()
        print("B")

B().hao()