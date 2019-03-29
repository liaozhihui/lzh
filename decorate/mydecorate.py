# coding=utf-8
import time
class Decorater(object):
    def __init__(self,func):
        self.func=func


    def __call__(self, *args, **kwargs):

       return self.calcute_time(*args, **kwargs)


    def calcute_time(self, *args, **kwargs):
        time1 = time.time()
        result=self.func(*args, **kwargs)
        time2 = time.time()
        print(self.func.__name__, "耗时", (time2 - time1))
        return result

