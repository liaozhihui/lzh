# coding=utf-8
from mydecorate import Decorater

@Decorater
def add(num):
    num_list=[]
    for i in range(num):
        num_list.append(i)
@Decorater
def add_append(num):
    num_list=[]
    num_list_append = num_list.append

    for i in range(num):
        num_list_append(i)
add(10000000)
add_append(10000000)