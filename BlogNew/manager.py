# coding=utf-8
"""
启动和项目管理的相关操作
"""
from app import create_app,db
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from app.models import *

#创建 app
app=create_app()
#创建 Manager对象用于管理app
manager=Manager(app)
#创建 Migrate对象用于关联要管理的app和db
migrate=Migrate(app,db)
#通过Manager对象增加的迁移指令
manager.add_command('db',MigrateCommand)


if __name__=="__main__":
    manager.run()
