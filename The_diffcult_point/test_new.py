# coding=utf-8
class Singon(object):



    def __new__(cls):

        print(object.__new__(cls))

        if not hasattr(cls,'instance'):

            cls.instance=object.__new__(cls)

        return cls.instance
    def __init__(self):
       pass
a=Singon()
b=Singon()
a.attr1="values"
print(a.attr1,b.attr1)
print(a==b)