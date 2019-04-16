# coding=utf-8
from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
import json

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
    def to_dict(self):
        dic={'id':self.id,'uphone':self.uphone,'upwd':self.upwd,'uname':self.uname,'uemail':self.uemail}
        return dic

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

@app.route("/05-json")
def json_views():
    obj1={
        'uname':'lvzemaria',
        'uage':'35',
        'ugender':'Male'
    }
    obj2 = {
        'uname': 'wei',
        'uage': '47',
        'ugender': 'Male'
    }
    obj3 = {
        'uname': 'menmen',
        'uage': '18',
        'ugender': 'Femail'
    }

    obj=(obj1,obj2,obj3)
    users = User.query.all()
    obj = [{"uname": u.uname, "upwd": u.upwd, "uemail": u.uemail, "uphone": u.uphone} for u in users]
    ulist=[]
    for user in users:
        ulist.append(user.to_dict)
    obj=[user.to_dict() for user in users]
    print("装换之前obj的数据类型为:",type(obj))
    jsonStr=json.dumps(obj)
    print("装换之后obj的数据类型为:", type(jsonStr))
    print("JSONStr:",jsonStr)

    return jsonStr

@app.route('/05-temp')
def temp_views():
    return render_template("05-json.html")

@app.route("/07-temps",methods=["POST","GET"])
def temp07():
    # uname=request.args['uname']
    # uage=request.args['uage']
    uname = request.form['uname']
    uage = request.form['uage']
    print('姓名%s年龄%s'%(uname,uage))
    return render_template("07-temp.html")
@app.route("/07-load")
def load_views():
    return render_template('07-load.html')

@app.route("/08-jq-get")
def get_views():
    return render_template('08-jq-get.html')

@app.route("/08-server")
def server08():
    #1、接收前段传递过来的参数
    uname = request.args['uname']
    #2、根据uname的值去数据库中查询对应的user的信息
    user=User.query.filter_by(uname=uname).first()
    if user:
        return json.dumps(user.to_dict())
    else:
        dic={
            "errMsg":"查无此人"
        }
        return json.dumps(dic)
@app.route("/09-show")
def show_views():
    return render_template("Email.html")

@app.route("/09-homework")
def homework09():
    #1、接收前段传递过来的参数
    email = request.args.get('email',"")
    if not email:
        return "0"
    print(email)
    #2、根据uname的值去数据库中查询对应的user的信息
    emails=db.session.query(User.uemail).filter(User.uemail.like("%"+email+"%")).all()
    if emails:
        return json.dumps(emails)
    else:

        return "0"


if __name__ == '__main__':
    manager.run()
