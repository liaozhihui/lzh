# coding=utf-8
from flask import Flask
#将当前的运行的主程序构建成Flask应用，以便接受用户的请求和响应1
app=Flask(__name__)

@app.route('/index')#匹配用户的访问路径
def index():
    return "This is may first flask demo"

@app.route('/')#匹配用户的访问路径
def first():
    return "<h1>这是网站首页</h1>"

if __name__=="__main__":
    #debug = True ,调试模式，真正部署运行时debug=False
    app.run(debug=True)