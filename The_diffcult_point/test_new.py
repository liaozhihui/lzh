# coding=utf-8
class Singon(object):



    def a(cls,a):
        if not hasattr(a,'isinstance'):

            a.instance=super(Singon,a).__new__(a)
        return a.instance

    def __init__(self):
        pass

a=Singon()
b=Singon()
a.a(Singon)