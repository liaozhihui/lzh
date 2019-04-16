# coding=utf-8
from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/province_city"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['DEBUG'] = True
#配置自动提交,每次在执行完视图处理函数时将自动提交操作回数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db=SQLAlchemy(app)

manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)
class Province(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    pname=db.Column(db.String(32))
    city=db.relationship('City',backref='province',lazy='dynamic')
    def to_dict(self):
        dict={'id':self.id,'pname':self.pname}
        return dict

class City(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    cname=db.Column(db.String(32))
    pid=db.Column(db.Integer,db.ForeignKey("province.id"))
    def to_dict(self):
        dict={'id':self.id,'cname':self.cname,'pid':self.pid}
        return dict

@app.route('/06-province')
def province_views():
    return render_template('06-province.html')

@app.route('/06-getPro')
def getpro_views():
    #读取province表中所有的数据并分装成JSON响应回去
    provinces=Province.query.all()
    list=[]
    for pro in provinces:
        list.append(pro.to_dict())
    return json.dumps(list)
@app.route('/06-getCity',methods=["POST"])
def getCity_views():
    pid=int(request.form['pid'])
    citys=City.query.filter_by(pid=pid).all()
    list=[city.to_dict() for city in citys]
    return json.dumps(list)
@app.route('/06-getCity1')
def getCity_views1():
    pid=int(request.args['pid'])
    citys=City.query.filter_by(pid=pid).all()
    list=[]
    for c in citys:
        list.append(c)
    return json.dumps(list)
if __name__ == '__main__':
    manager.run()