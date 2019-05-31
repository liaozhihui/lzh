# coding=utf-8
from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from sqlalchemy import or_,func
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

'''
create table student(id int not null AUTO_INCREMENT primary key, 
name varchar(20) not null unique, 
age int)default charset=utf8;

insert into student (name,age) values ('小明',12) on duplicate key update name=values(name),age=values(age);

'''
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
    wife=db.relationship('Wife',backref='user',uselist=False)
    def __repr__(self):
        return "<User:%r>"%self.username

class Wife(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    wname=db.Column(db.String(30))
    #增加外检约束和唯一约束
    uid=db.Column(db.Integer,db.ForeignKey('users.id'),unique=True)

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
    #增加外键列,要引用自course表的主键id
    cid = db.Column(db.Integer,db.ForeignKey('course.id'))
    students=db.relationship("Student",lazy='dynamic',secondary='student_teacher'
                             ,backref=db.backref('teachers',lazy="dynamic"))

class Student_teacher(db.Model):
    __tablename__='student_teacher'
    id=db.Column(db.Integer,primary_key=True)
    student_id=db.Column(db.Integer,db.ForeignKey("student.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))




class Course(db.Model):
    __tablename__="course"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    cname=db.Column(db.String(30),nullable=False,unique=True,index=True)
    #准备增加关联属性和反向引用关系属性,backref是插入Teacher中
    teachers=db.relationship("Teacher",backref="course",lazy="dynamic")
    #增加关联属性与反向引用关联属性（Course与Student之间的多对多）
    students=db.relationship('Student',lazy='dynamic',#lazy针对Course类中的students属性的延迟加载
                             backref=db.backref("courses",lazy='dynamic')#lazy针对Student类中的courses属性的延迟加载
                             ,secondary="student_course") #指定第三张关联表



#编写StudentCourse类，表示的是Student与Course之间的关联类(表)
#表名:student_course
class StudentCourse(db.Model):
    __tablename__='student_course'
    id = db.Column(db.Integer,primary_key=True)
    #外键:student_id,引用自student表的主键id
    student_id=db.Column(db.Integer,db.ForeignKey('student.id'))
    #外键course_id,引用自course表的主键id
    course_id=db.Column(db.Integer,db.ForeignKey('course.id'))

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
    print(request.args.get('id',-5))
    search = request.args.get('search','')
    pageSize=15
    totalPageSize=db.session.query(Users).filter(or_(Users.username.like('%'+search+'%'),
                       Users.email.like('%' + search + '%'))).count()

    lastPage = math.ceil(totalPageSize/pageSize)

    page=int(request.args.get('page','1'))

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

@app.route('/06-aggregate')
def aggragate_view():
    # result=db.session.query(func.sum(Users.age)).all()
    #查询Users实体类中所有人的平均年龄，年龄总和，最大年龄和最小年龄分别都是多少
    # result=db.session.query(func.avg(Users.age),func.sum(Users.age),func.max(Users.age)).all()
    result = db.session.query(Users.isActive,func.avg(Users.age).group_by('isActive')).having(func.avg(Users.age)>=18).all
    print(result)
    return "聚合查询成功"
@app.route('/07-aggregate-exer')
def aggregate_exer():
    #查询Users中的总年龄
    db.session.query(func.sum(Users.age)).all()
    #查询User实体中年龄大于18岁的人的平均年龄是多少
    db.session.query(func.avg(Users.age)).filter(Users.age>18).all()
    #查询Users实体中总人数是多少
    db.session.query(func.count(Users.id)).all()
    #查询Users实体中按isActive分组后，组内人数大于2人的组的信息(组，人数)
    db.session.query(Users.isActive,func.count('*')).group_by('isActive').having(func.count('*')>2)
    #查询Users实体中年龄大于18岁的人按isActive分组后，组内人数大于2恩的组的信息（组,人数）
    db.session.query(Users.isActive, func.count('*')).filter(Users.age>18).group_by('isActive').having(func.count('*') > 2)

@app.route('/delete')
def delete_view():
    id=request.args['id']
    search = request.args.get('search', '')
    print(id)
    user=Users.query.filter_by(id=id).first()
    db.session.delete(user)
    return redirect('/queryall?search=%s' % search)
    # return "<script>alert('删除成功');location.href='/queryall?search=%s'</script>"%search
@app.route('/modify',methods=['POST','GET'])
def modify_view():

    if request.method=="GET":
        id = request.args['id']
        search = request.args.get('search', '')
        user = Users.query.filter_by(id=id).first()
        return render_template('modify.html',user=user,sea=search)
    else:
        id = request.form['id']
        search = request.form.get('search', '')
        user = Users.query.filter_by(id=id).first()
        user.username = request.form['username']
        user.email = request.form['email']
        user.age = request.form['age']
        user.isActive = False
        if 'isActive' in request.form:
            user.isActive = True
        db.session.add(user)
        return redirect('/queryall?search=%s'%search)
        # return "<script>alert('修改成功');location.href='/queryall?search=%s'</script>"%search


@app.route('/10-regtea')
def regtea_views():
    #方案1：声明一个Teacher对象，通过外键属性来关联对应的course的id值
    # tea=Teacher()
    # tea.sname="小红"
    # tea.sage=18
    # tea.cid=2
    # db.session.add(tea)

    #方案2：声明一个Teacher对象，通过course属性来关联对应的course
    tea=Teacher()
    tea.sname='老魏Maria'
    tea.sage=47
    #获取id为1的课程信息
    course=Course.query.filter_by(id=1).first()
    #将course对象的与tea对象关联
    tea.course=course
    db.session.add(tea)
    return "注册teacher成功"
@app.route('/11-query')
def query11_views():
    #1、查询lzmaria老师的个人信息以及所教授的课程
    tea=Teacher.query.filter_by(sname='lzmaria').first()
    print("姓名：%s,年龄:%d"%(tea.sname,tea.sage))
    print("所教课程:%s"%tea.course.cname)
    #查询python所对应的所有的老师的信息
    course=Course.query.filter_by(cname='python').first()
    print("课程名称:%s"%course.cname)
    #通过course中的关联属性teachers来获取对应的所有的老师的信息


    #course.teachers表示的是course所对应的teachers的一个查询对象(AppenderBaseQuery类型，属于BaseQuery的一个子类)
    print(type(course.teachers))
    teachers = course.teachers.all()
    print(teachers)
    return "查询陈宫"
@app.route('/12-regteacher',methods=['GET','POST'])

def regteacher():
    if request.method=='GET':
        courses=Course.query.all()
        return render_template('12-regteacher.html',courses=courses)
    else:
        tname=request.form['tname']
        tage=request.form['tage']
        cid=request.form['cid']
        tea=Teacher()
        tea.sname=tname
        tea.sage=tage
        db.session.add(tea)
        return "注册成功"
@app.route('/13-queryteacher')

def queryteacher():
    courses=Course.query.all()
    cid=request.args.get('cid','0')
    if cid=='0':
        teachers=Teacher.query.all()

        pass
    else:
        teachers=Course.query.filter_by(id=cid).first().teachers.all()
    return render_template('13-queryteacher.html',courses=courses,teachers=teachers)
    return "注册成功"
@app.route('/14-oto')
def oto_views():
    # wife=Wife()
    # wife.wname='Maira夫人'
    # wife.uid=1
    # db.session.add(wife)
    wife=Wife.query.filter_by(id=1).first()
    user=wife.user
    print('wife:',wife.wname)
    print('user:',user.username)

    return "查询wife成功"
@app.route('/15-wiferegister',methods=['GET','POST'])
def wiferegister():
    users = Users.query.all()
    if request.method=='GET':
        users=Users.query.all()
        return render_template('wiferegister.html',users=users)
    else:
        wifes=Wife.query.all()
        # usersList=[wife.user for wife in wifes]

        wname=request.form['wname']
        userid=int(request.form['wuser'])
        user=Wife.query.filter_by(id=userid).first()
        if not user:
            wife = Wife()
            wife.wname=wname
            wife.user=user
            db.session.add(wife)
            return redirect('/showWife')
        else:
            return "<script>alert('注册失败');location.href='/15-wiferegister'</script>"

@app.route('/showWife')
def showWife():
    wifes=Wife.query.all()
    return render_template('showWife.html',wifes=wifes)
@app.route("/16-mtm")
def mtm_views():
    #向第三张表中插入关联数据
    #演示：如何将student对象和course对象关联到一起
    #语法：关联属性/反向引用关系属性 都提供了一个方法append() 用户关联两张表中的数据到第三表中
    #查询Tom的信息，
    stu=Student.query.filter_by(sname='Tom').first()
    # 查询python的课程信息
    cou=Course.query.filter_by(cname='python').first()
    #方案一：通过stu属性courses将cou关联
    stu.courses.append(cou)
    #方案二：通过cou属性students将stu关联
    return "插入关联数据成功"

@app.route("/17-mtm-query")
def mtmquery_views():
    #查询 id 为1的course的信息
    course=Course.query.filter_by(id=1).first()
    #再查询course对应的student列表
    students=course.students.all()
    for stu in students:
        print("学员的姓名:"+stu.sname)
    return "数据查询成功"

@app.route('/studentregister',methods=["POST","GET"])
def regstudent():
    if request.method=="GET":
        courses=Course.query.all()
        return render_template("studentregister.html",courses=courses)
    else:
        student=Student()
        student.sname=request.form['sname']
        student.sage = request.form['sage']
        courseList=request.form.getlist('courses')

        list=Course.query.filter(Course.id.in_(courseList)).all()
        db.session.add(student)
        db.session.commit()
        for course in list:
            student.courses.append(course)
        return "注册成功"
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