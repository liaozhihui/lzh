# coding=utf-8
"""
此处编写的是有关topic的路由和视图(业务逻辑处理)
"""
from . import topic
from flask import render_template,request,session,redirect
import sys,os
import datetime

from .. import db
from ..models import *

@topic.route('/')
def topic_index():
    category=db.session.query(Category).all()
   #2、判断session中是否有登录信息，有的话则取出对应的对象
    #3、查询topic中前20条数据放在首页中进行显示
    topics= Topic.query.limit(20).all()
    print(topics)
    user = None
    if 'id' in session and 'loginname' in session:
        id = session['id']
        user = User.query.filter_by(ID=id).first()
    return render_template("index.html",category=category,user=user,topics=topics)

@topic.route('/list')
def topic_list():
    id=request.args['id']
    return render_template("index.html",id=id)


@topic.route("/release",methods=['GET','POST'])
def release_views():
    if request.method == "GET":
        if 'id' in session and 'loginname' in session:
            #有登录用户则判断是否有权限
            user = User.query.filter_by(ID=session['id']).first()
            if user.is_author:
                #查询Category的所有的信息
                cates=Category.query.all()

                return render_template('release.html',cates=cates)
        return redirect('/')
    else:
        #执行发表博客的相关操作
        #1、创建topic对象
        topic = Topic()
        #2、接收前端传递过来的值并赋值给topic对象
        #2.1接收标题author，赋值给topic.title
        topic.title=request.form['author']
        #2、2接收类型list,赋值给topic.blogtype_id
        topic.blogtype_id=request.form['list']
        #2、3接收内容类型cate,赋值给topic.category_id
        topic.category_id = request.form['cate']
        #2.4从session中获取登录id,赋值给topic.user_id
        topic.user_id = session['id']
        #2.5获取系统时间，赋值给topic.pub_date
        topic.pub_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #2.6获取发表的内容content并赋值给topic.content
        topic.content = request.form['content']
        #2.7判断是否有上传文件，如果有的话实现上传并将路径赋值给topic.images
        if request.files:
            #1、有文件上传
            f = request.files['picture']
            #2、处理文件上传路径
            ftime=datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            ext = f.filename.split('.')[-1]
            filename=ftime+'.'+ext
            print(filename)
            #3、处理文件的上传路径
            topic.images = 'upload/' + filename
            #并为topic.images赋值
            #4、拼出完整的保存路径(绝对路径)
            basedir=os.path.dirname(os.path.dirname(__file__))
            upload_path = os.path.join(basedir,'static/upload',filename)
            #5、保存文件到指定目录处
            f.save(upload_path)
        db.session.add(topic)
        return redirect('/')

print("views")
