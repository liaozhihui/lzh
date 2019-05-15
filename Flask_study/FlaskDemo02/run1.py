# coding=utf-8
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/01-var')
def show():
    return render_template('01-var.html',groupName="保健三人组",name1="lvze",\
                         name2='伟明泽',name3="王党波")
@app.route('/02-var')
def var02():
    #字符串
    name="Mengmeng"
    #数字
    age=80
    #列表，元祖，字典
    list=['吕泽','老魏','淡泊']
    tup=('萌萌','隔壁老王')
    dic={'NAYTO':'鸣人',
         'SASUKE':'佐助',
         'SAKURA':'小樱'
         }
    #对象
    person = Person()
    person.name='   为老同sf '
    #locals()用户获取局部变量组成一个字典
    return render_template('02-var.html',params=locals())
@app.route('/03-macro')
def macro():
    list=['wo','shi','liao','zhi','hui']
    return render_template('03-macro.html',list=list)

@app.route('/04-static')
def static_views():
    return render_template('04-static.html')

@app.route('/05-parent')
def parent():
    return render_template('05-parent.html')

@app.route('/06-child')
def child():
    return render_template('06-child.html')

class Person(object):
    name='老魏'
    def hobby(self):
        return self.name+"喜欢玩王者荣耀"

if __name__=="__main__":
    app.run(debug=True)