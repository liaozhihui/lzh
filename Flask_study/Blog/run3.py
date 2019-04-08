# coding=utf-8
from flask import Flask,render_template,request
import os,datetime
app=Flask(__name__)

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



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')