# coding=utf-8
from flask import Flask,render_template,request
import os,datetime
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
import pymysql
pymysql.install_as_MySQLdb()
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost:3306/blog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['DEGUB'] = True
db = SQLAlchemy(app)

manager=Manager(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/list")
def list():
    return render_template('index_.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method =="GET":
        return render_template('login.html')
    else:
        username=request.form.get("username")
        password=request.form.get("password")
        return str(locals())
@app.route('/register',methods=["GET","POST"])
def register():
    if request.method =="GET":
        return render_template('register.html')
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        password = request.form.get("url")

        return str(locals())

@app.route('/release',methods=['GET','POST'])

def realse():
    if request.method == 'GET':
        return render_template("release.html")
    else:
        listtype=request.form.getlist('list')
        content = request.form.get('content')
        title = request.form.get('author')
        print(request.files)


        if '.' in request.files:
            files = request.files['picture']
            ext = files.filename.split('.')[-1]
            # 3、获取当前的时间：YYYYMMDDHHMMSSFFFFFF
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            # 4、将时间和扩展名拼到一起，组成新的文件名
            filename = ftime + '.' + ext
            # 5、将文件上传到static/upload目录下
            # picture.save('static/upload/'+filename)
            # 使用绝对路径来上传路径
            # /home/csdn/AID/lzh/Flask_study/FlaskDemo04/static
            basedir = os.path.dirname(__file__)

            upload_path = os.path.join(basedir, 'static/upload', filename)
            files.save(upload_path)
        return str(locals())

class Users(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    url =db.Column(db.String(120),nullable=True)
    password=db.Column(db.String(100),nullable=False)

if __name__=="__main__":
    # app.run(debug=True,host='0.0.0.0')
    migrate=Migrate(app,db)
    manager.add_command('db', MigrateCommand)
    manager.run()

