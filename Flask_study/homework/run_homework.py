# coding=utf-8
from flask import Flask, render_template, request
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:123456@localhost:3306/homework'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config["DEBUG"]=True
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] =True

db=SQLAlchemy(app)
manager=Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)

class Teacher(db.Model):
    __tablename__="teacher"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    sname=db.Column(db.String(30),nullable=False)
    sage=db.Column(db.Integer,nullable=False)
    isActive=db.Column(db.Boolean,default=True,nullable=False)
    #增加外键列,要引用自course表的主键id
    cid = db.Column(db.Integer,db.ForeignKey('course.id'))


class Course(db.Model):
    __tablename__="course"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    cname=db.Column(db.String(30),nullable=False,unique=True,index=True)
    #准备增加关联属性和反向引用关系属性,backref是插入Teacher中
    teachers=db.relationship("Teacher",backref="course",lazy="dynamic")

@app.route('/')
def index():
    return "这是首页"
@app.route('/register',methods=['GET','POST'])
def register_views():
    if request.method=="GET":
        courses=Course.query.all()

        return render_template("register.html",courses=courses)
    else:
        teacher=Teacher()
        teacher.sname=request.form['sname']
        teacher.sage=request.form['sage']
        teacher.cid=request.form['cid']
        isActive=False

        if 'isActive' in request.form:
            isActive=True
        teacher.isActive=isActive
        db.session.add(teacher)
        return "注册成功"
@app.route('/select',methods=["GET","POST"])
def select_views():

    id=int(request.args.get('course',0))
    teachers = Teacher.query.all()
    courses = Course.query.all()
    print(id)

    if id != 0:
        courses = Course.query.all()
        course = Course.query.filter_by(id=id).first()
        teachers=course.teachers.all()
    return render_template("course.html",sel=id, courses=courses, teachers=teachers)




if __name__=="__main__":
    manager.run()
