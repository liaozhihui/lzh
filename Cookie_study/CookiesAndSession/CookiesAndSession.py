# coding=utf-8

from flask import Flask,make_response,request,render_template,session
from flask_script import Manager
#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']="aiaxieshaxiesha"
manager=Manager(app)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/01-setcookie')
def setcookie():
    resp=make_response("保存cookie成功")
    # 保存时长小于等于0相当与删除cookie，不设置时长表示只在会话期间有效
    resp.set_cookie("username1","xiaozemaria1",60*60*24*365*3)
    #保存时长等于0相当与删除cookie
    return resp

@app.route('/02-getcookie')
def getcookie():
    if "username" in request.cookies:
        username=request.cookies['username']

        print(request.cookies[username])
    return "查询cookies成功"
@app.route('/03-sign-in',methods=["POST","GET"])
def sign_in():
    if request.method=="GET":
        if 'uname' in request.cookies and 'pwd' in request.cookies:
            uname=request.cookies['uname']
            pwd=request.cookies['pwd']
            if uname =='admin' and pwd=='admin':

                return "欢迎%s回来"%uname
            else:
                resp=make_response(render_template('03-sign-in.html'))
                resp.delete_cookie('uname')
                resp.delete_cookie('pwd')
                return resp
        else:

            return render_template('03-sign-in.html')
    else:
        name=request.form['uname']
        pwd=request.form['pwd']

        if name=='admin' and pwd=='admin':
            resp = make_response("登录成功")
            print(request.form)
            print(request.cookies)
            if 'rem' in request.form:
                resp=make_response("登录成功")
                resp.set_cookie("uname",name,60*60)
                resp.set_cookie("pwd", pwd,60*60)

            return resp
        else:
            return "登录失败"
@app.route('/04-setsession')
def setsession():
    session['uname']='maria'
    session['upwd']='xiaoze'
    return "保存session成功"
@app.route("/05-getsession")
def getsession():
    #建议：获取session之前先做判断
    if 'uname' in session:
        uname=session['uname']
        print("用户名称："+uname)
    upwd = session.get('upwed','')
    print("用户密码"+upwd)
    return "获去取session成功"

@app.route("/06-session-login",methods=["GET","POST"])
def session_login_views():
    if request.method=="GET":
        if session:
            uname=session['uname']
            upwd=session['upwd']
            return "欢迎%s回来"%uname
        else:
            if request.cookies:
                uname = request.cookies['uname']
                upwd = request.cookies['upwd']
                session['uname'] = uname
                session['upwd'] = upwd
                return "欢迎%s回来"%uname
            else:
                return render_template("session_login.html")
    else:
        uname=request.form['uname']
        upwd=request.form['upwd']
        if uname=='admin' and upwd=='upwd':
            session['uname'] = uname
            session['upwd'] = upwd
            res = make_response("登录成功")
            if 'rem' in request.form:

                res.set_cookie("uname",uname,60*60*365)
                res.set_cookie("upwd", upwd, 60 * 60 * 365)
            return res
        else:
            return "登录失败1"

if __name__ == '__main__':
    manager.run()

