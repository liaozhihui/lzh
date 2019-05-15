# coding=utf-8
import sys
sys.path.append('/home/csdn/AID/lzh/decorate')
from mydecorate import Decorater
@Decorater
def pri():
    print("test_dot")

pri()