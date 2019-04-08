#coding:utf-8

from flask import Flask,request,render_template
import datetime,random,os

app = Flask(__name__)

@app.route('/01-file',methods=["GET","POST"])
def file_views():
    if request.method == 'GET':
        return render_template('01-file.html')
    else:
        #1、获取前段传递过来的文件
        picture = request.files['picture']
        #2、得到文件的名称(扩展名)
        ext=picture.filename.split('.')[-1]
        #3、获取当前的时间：YYYYMMDDHHMMSSFFFFFF
        ftime=datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        #4、将时间和扩展名拼到一起，组成新的文件名
        filename = ftime + '.' + ext
        #5、将文件上传到static/upload目录下
        # picture.save('static/upload/'+filename)
        #使用绝对路径来上传路径
        #/home/csdn/AID/lzh/Flask_study/FlaskDemo04/static
        basedir=os.path.dirname(__file__)
        print(basedir)
        upload_path=os.path.join(basedir,'static/upload',filename)
        picture.save(upload_path)
        return "头像上传成功"


if __name__=="__main__":
    app.run(debug=True)