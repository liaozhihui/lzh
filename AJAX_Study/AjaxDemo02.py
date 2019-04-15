# coding=utf-8
from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/ajax"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['DEBUG'] = True
#配置自动提交,每次在执行完视图处理函数时将自动提交操作回数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db=SQLAlchemy(app)

manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    uname=db.Column(db.String(32),nullable=False)
    upwd=db.Column(db.String(32),nullable=False)
    uphone=db.Column(db.String(32),unique=True,nullable=False)
    uemail=db.Column(db.String(32),nullable=False)

@app.route('/test')
def hello_world():
    print(request.args.get('id',-1))
    return redirect('/02-test')

@app.route('/02-test')
def test02():
    print(request.args.get('id',-1))
    return "end"


@app.route('/01-ajax-get')
def  ajax_get():
    return render_template('01-ajax-get.html')
@app.route('/01-server')
def server():
    return "这是使用ajax的方式发送的请求"

@app.route('/reUser',methods=["GET","POST"])
def reUser_view():
    if request.method=="GET":
        return render_template("reUser.html")
    else:
        user=User()
        user.uname=request.form['uname']
        user.uphone=request.form['uphone']
        user.upwd=request.form['upwd']
        user.uemail=request.form['uemail']
        db.session.add(user)
        return "<script>alert('注册成功');location.href='/reUser'</script>"

@app.route('/02-checkuphone')
def checkuphone():
    return render_template('02-checkuphone.html')

@app.route('/02-server')
def server02():
    uphone=request.args['uphone']
    print(uphone)
    user=User.query.filter_by(uphone=uphone).first()
    print(user)
    if user:
        return "电话号码已存在"
    else:
        return "通过"

@app.route('/02-myserver')
def myserver02():
    uphone=request.args['uphone']

    user=User.query.filter_by(uphone=uphone).first()

    if user:
        return "1"
    else:
        return "通过"

@app.route('/03-post')
def post_views():
    return render_template("03-post.html")

@app.route('/03-server01',methods=["POST"])
def server031():
    #接收前段传递过来的数据
    uname=request.form['uname']
    upwd=request.form['upwd']
    #将数据在响应回去
    str="用户名:%s,密码:%s"%(uname,upwd)
    return str

@app.route('/03-server02',methods=["POST"])
def server032():
    uname=request.form['uname']
    upwd = request.form['upwd']
    str="用户名：%s,密码:%s"%(uname,upwd)
    return str
if __name__ == '__main__':
    manager.run()
