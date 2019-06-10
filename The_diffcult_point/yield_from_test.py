# coding=utf-8
from itertools import chain

my_list=[1,2,3]
my_dict={"Bobby1":"http://projectsedu.com",
         "Bobby2":"http://www.imooc.com"}

# def g1(iterable):
#     yield iterable
#
# def g2(iterable):
#     yield from iterable
#
# for value in g1(range(10)):
#     print(value)
#
# for value in g2(range(10)):
#     print(value)
#
# def my_chain(*args,**kwargs):
#     for my_iterable in args:
#         yield from my_iterable
#
# for value in my_chain(my_list,my_dict,range(5,10)):
#     print(value)
# def g1(gen):
#     yield from gen
# def main():
#     g=g1()
#     g.send(None)

#1、main调用方,g1(委托生成器),gen(子生成器)
#2、yield from 会调用方与子生成器之间建立双向通道
# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total/count

# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()

# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激下生成器
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0

if __name__ == '__main__':
    main()
