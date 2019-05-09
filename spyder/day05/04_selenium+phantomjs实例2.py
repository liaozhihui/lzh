
from selenium import webdriver
import time
#创建phantomjs浏览器对象
driver=webdriver.PhantomJS(executable_path="./phantomjs/bin/phantomjs")
#用get方法请求("http://www.baidu.com/")
driver.get("http://www.baidu.com/")
#查看相应内容:
html=driver.page_source
print(html)
#向搜索框输(id kw)入赵丽颖
driver.find_element_by_id("kw").send_keys("赵丽颖")
print(111)
time.sleep(5)
#点击百度一下按钮(id su)
driver.find_element_by_id("su").click()
#截图
driver.save_screenshot("ying.png")
#关闭浏览器
driver.quit()