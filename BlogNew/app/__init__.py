# coding=utf-8
"""
当前程序的初始化操作
主要工作：
1、构建Flask应用实例以及各种配置
2、创建SQLALCHEMY实例
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#声明SQLALchemy的实例 - db
db = SQLAlchemy()

def create_app():
    #1、创建Flask的应用 - app
    app=Flask(__name__)
    #2、为app 设置各种配置
    #配置启动模式为调试模式
    app.config["DEBUG"]=True
    #配置数据库的连接信息
    app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123456@localhost:3306/blognew"
    #配置数据库的自动提交
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    #配置信号追踪
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #配置session所需要的secret_key,是为了配置session
    app.config["SECRET_KEY"] = "AIXIESHAXIESH"

    #关联db 和 app
    db.init_app(app)
    #将topic蓝图程序与app进行关联
    from .topic import topic as topic_blueprint
    from .users import users as users_blueprint
    app.register_blueprint(topic_blueprint)
    app.register_blueprint(users_blueprint)
    #3、返回app
    return app

if __name__=="__main__":
    app=create_app()
    app.run()