# coding=utf-8
"""
实现topic程序包的初始化操作
"""
from flask import Blueprint
topic=Blueprint("topic",__name__)
from . import views
print("init")
