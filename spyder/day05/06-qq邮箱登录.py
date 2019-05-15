# coding=utf-8
from selenium import webdriver
import time
browser = webdriver.PhantomJS()
browser.get("https://mail.qq.com/")
login_frame = browser.find_element_by_id("login_frame")
browser.switch_to_frame(login_frame)

#输入qq号 密码 点击登录按钮
uname=browser.find_element_by_xpath('//*[@id="u"]')
uname.send_keys('1581627402')
upwd= browser.find_element_by_xpath('//*[@id="p"]')
upwd.send_keys("lzh911128")

login = browser.find_element_by_xpath('//*[@id="login_button"]')

print(login.get_attribute("value"))

login.click()
time.sleep(2)
browser.save_screenshot('login.png')

browser.quit()