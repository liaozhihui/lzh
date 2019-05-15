# coding=utf-8

from . import users
from flask import request,render_template,session,redirect
from .. import db
from ..models import *
@users.route('/login',methods=["GET","POST"])
def user_index():

    if request.method == "GET":
        #判断已经处于登录状态上
        if 'id' in session and 'loginname' in session:
            return redirect('/')
        #获取请求源地址，保存进session，用于登录成功后的时候去使用，如果没有请求源地址
        #则将保存进session
        url = request.headers.get("Referer",'/')
        session['url']=url
        return render_template("login.html")
    else:
        loginname=request.form['username']
        upwd = request.form['password']
        user=User.query.filter_by(loginname=loginname,upwd=upwd).first()
        if user:
            session['id'] = user.ID
            session['loginname'] = loginname
            url=session['url']
            return redirect(url)

        else:
            return render_template('login.html')

