# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

#导入pymysql并且将其伪装成MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
#两种方式解决mysql:
# 1、导入pymysql并且将其伪装成MySQLdb
# 2、在uri中加入pymsql,如：mysql+pymysql://root:123456@localhost:3306/flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost:3306/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['DEGUB'] = True
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