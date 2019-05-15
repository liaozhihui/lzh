# coding=utf-8
# class test(object):
#     a=1
#
#     def __init__(self):
#         print(self.a)
#         self.a=3
#         print(self.a)
#
# test()
# print(test.a)
def a():
    print(1)
    for i in range(10):
        print(i)
        yield b(i,a)

def b(i,f):
    f()

for i in range(10):
    a()

