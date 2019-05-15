# coding=utf-8
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.set_headless
browser = webdriver.Chrome(options=options)
browser.get("http://www.baidu.com/")
browser.save_screenshot("baidu.png")
