# coding=utf-8
from selenium import webdriver

browser=webdriver.PhantomJS()

browser.get("https://www.qiushibaike.com/text/")

#单元素查找

div = browser.find_element_by_class_name('content')
print(div.text)

#多元素查找
divs=browser.find_elements_by_class_name('content')
for div in divs:
    #text是获取当前节点对象中所有文本内容(所有节点)
    print(div.text)
    print("*"*50)