# coding=utf-8
from bs4 import BeautifulSoup
import lxml
html = '''
<div class="test1">雄霸</div>
<div class="test1">灭霸</div>
<div class="test3">
<span>步惊云</span>
</div>
'''

soup = BeautifulSoup(html,'lxml')
r_list =soup.find_all('div',attrs={"class":"test1"})
print(r_list)

for r in r_list:
    print(r.get_text())

r_list = soup.find_all('div',{'class':'test3'})

for r in r_list:
    # print(r.get_text())
    print(r.span.string)