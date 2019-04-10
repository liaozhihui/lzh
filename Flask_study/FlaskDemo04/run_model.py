# coding=utf-8
from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from sqlalchemy import or_
import math
#导入pymysql并且将其伪装成MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
#两种方式解决mysql:
# 1、导入pymysql并且将其伪装成MySQLdb
# 2、在uri中加入pymsql,如：mysql+pymysql://root:123456@localhost:3306/flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost:3306/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['DEBUG'] = True
#配置自动提交,每次在执行完视图处理函数时将自动提交操作回数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)

#将app交给manager进行管理，以后由manager来启动程序
manager=Manager(app)

#创建实体类-Users,映射到数据库中users表
#id,主键,自增
#username,长度为80的字符串，不允许为空，唯一，加索引
#age,整数,允许为空
#email,长度为120的字符串，必须唯一
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False, unique=True, index=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True)
    isActive = db.Column(db.Boolean,default=True)
    def __repr__(self):
        return "<User:%r>"%self.username

class Student(db.Model):
    __tablename__="student"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    sname=db.Column(db.String(30),nullable=False)
    sage=db.Column(db.Integer,nullable=False)
    isActive=db.Column(db.Boolean,default=True,nullable=False)

class Teacher(db.Model):
    __tablename__="teacher"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    sname=db.Column(db.String(30),nullable=False)
    sage=db.Column(db.Integer,nullable=False)
    isActive=db.Column(db.Boolean,default=True,nullable=False)

class Course(db.Model):
    __tablename__="course"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    cname=db.Column(db.String(30),nullable=False,unique=True,index=True)


# db.drop_all()
# #通过db.create_all()将User类映射到数据库上
# db.create_all()

@app.route("/")
def index():

    return "这是我的Flask程序中的首页"

@app.route("/01-add")
def add_views():
    #创建user的对象
    #将Users的对象保存会数据库并提交
    user=Users()
    user.username='lzh'
    user.age=10
    user.email='maria@qq.com'
    db.session.add(user)

    return "增加数据成功"

@app.route('/02-register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('02-register.html')
    else:
        #创建Users对象
        user=Users()
        #接收前段传递过来的数据
        user.username=request.form['username']
        user.email=request.form['email']
        user.age=request.form['age']
        user.isActive=False
        if 'isActive' in request.form:
            user.isActive=True
        #将对象保存回数据库
        db.session.add(user)
    return "注册成功"
@app.route("/03-query")
def query_view():
    #查询Users中的所有的数据
    # query=db.session.query(Users)
    # print(query)
    # print("类型为：",type(query))
    users = db.session.query(Users).all()
    print(users)
    for user in users:
        print("姓名：%s,邮箱:%s"%(user.username,user.email))
    return "查询数据成功"
@app.route("/04-query")
def query04_view():
    #查询Users中的所有的数据
    # query=db.session.query(Users)
    # print(query)
    # print("类型为：",type(query))
    # users = db.session.query(Users).filter(Users.age.between(30,40)).all()
    #查询id =1的Users的信息
    users=db.session.query(Users).filter_by(id=1).first()
    users=db.session.query(Users).filter_by(id=1).first()

    print(users)

    return "查询数据成功"

@app.route("/queryall",methods=['GET','POST'])
def queryall_view():
    #查询Users中的所有的数据
    # query=db.session.query(Users)
    # print(query)
    # print("类型为：",type(query))
    search = request.args.get('search','')
    pageSize=3
    totalPageSize=db.session.query(Users).filter(or_(Users.username.like('%'+search+'%'),
                       Users.email.like('%' + search + '%'))).count()
    print(totalPageSize)
    lastPage = math.ceil(totalPageSize/pageSize)
    print(lastPage)
    page=int(request.args.get('page','1'))
    print(page)
    prevPage=1
    if page>1:
        prevPage=page-1

    nextPage=totalPageSize
    if page<nextPage:
        nextPage=page+1
    if page>=lastPage:
        page=lastPage
    if search:
        users=db.session.query(Users).\
            filter(or_(Users.username.like('%'+search+'%'),
                       Users.email.like('%' + search + '%')))\
            .offset((page-1)*pageSize).limit(pageSize).all()
    else:
        users = db.session.query(Users) \
            .offset((page - 1) * pageSize).limit(pageSize).all()

    return render_template('queryall.html',users=users,
                           sea=search,lastPage=lastPage,
                           page=page,prevPage=prevPage,nextPage=nextPage,totalPageSize=totalPageSize)
@app.route('/04-query')
def query04_views():
    #1、查询age>40并且isActive为True的Users的信息
    users=db.session.query(Users).filter(Users.age>40,Users.isActive==True).all()
    # 2、查询age>40或者isActive为True的Users的信息
    users = db.session.query(Users).filter(or_(Users.age > 40, Users.isActive == True)).all()
    print(users)
    return "查询数据成功"

@app.route('/05-page')

def page_view():
    #变量-pageSize,表示每页显示的记录数量
    pageSize=2
    #接收前段传递过来的参数 -page,表示想看的页数是第几页
    page=int(request.args.get('page','1'))
    userlist=db.session.query(Users).offset((page-1)*pageSize).limit(pageSize).all()
    #通过pageSize和总记录数计算尾页码
    totalCount=db.session.query(Users).count()
    #通过totalCount和pageSize计算尾页，将结果保存在lastPage变量中
    lastPage=math.ceil(totalCount/pageSize)
    #通过page计算上一页(prevPage)和下一页nextPage
    prevPage=1

    if page>1:
        prevPage = page -1
    nextPage=lastPage
    if nextPage<lastPage:
        nextPage=page+1
    # return '每页显示%d条数据，当前要看的页数为%d页'%(pageSize,page)
    return render_template('05-page.html',users=userlist,lastPage=lastPage,
                           prevPage=prevPage,nextPage=nextPage)
    pass

if __name__=="__main__":
    #将使用manager来启动程序
    # manager.run()

    # app.run(debug=True)
    #问1、debug模式无法启动
    #解决方案:app.config['DEBUG'] = True
    #无法指定启动的窗口
    #解决方案：python3 run.py runserver --port xxx
    #指定启动的ip地址
    #解决方案：python3 run.py runserver --host 0.0.0.0 --port xxx

    #创建Migrate对象，指定关联的app和db
    migrate=Migrate(app,db)
    #为manager增加子命令，增加做数据库迁移的子命令
    #为manager增加一个叫做db的子命令，该命令的具体执行操作由MigrateCommond来提供
    manager.add_command('db',MigrateCommand)
    manager.run()