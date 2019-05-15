
from selenium import webdriver
#创建phantomjs浏览器对象
driver=webdriver.PhantomJS(executable_path="./phantomjs/bin/phantomjs")
#用get方法请求("http://www.baidu.com/")
driver.get("http://www.baidu.com/")
#获取截图
driver.save_screenshot("百度.png")
#关闭浏览器
driver.quit()