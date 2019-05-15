# coding=utf-8
from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/01-test")
def test_view():
    return render_template('01-test.html')

@app.route("/01-request")
def request_views():
   print("scheme:",request.scheme)
   print("method:", request.method)
   print("args:", request.args)
   print("form:", request.form)
   print("cookies:", request.cookies)
   print("files:", request.files)
   print("path:", request.path)
   print("full_path:", request.full_path)
   print("url:", request.url)
   print("headers:", request.headers)
   #获取Referer请求消息头
   if 'Referer' in request.headers:
       print("请求原地址",request.headers['Referer'])


   return "获取request成功"
@app.route("/02-get")
def get_view():
    return render_template('02-get.html')

@app.route("/02-server")
def server02():
#通过request.args获取请求提交的数据
    uname = request.args.get('uname')
    upwd=request.args['upwd']
    gender = request.args.get('gender')
    hobby=request.args.getlist('hobby')
    print(locals())
    return "获取请求数据成功"
@app.route("/03-get-exer")
def get_exer():
    return render_template('get-exer.html')

@app.route("/03-server")
def server03():
    title=request.args.get('title')
    classs=request.args['class']
    content=request.args.get('content')
    print(locals())
    return "获取数据成功"

@app.route('/04-post')
def post_views():
    return render_template('04-post.html')

@app.route('/04-server',methods=['POST'])
def server04():
    uname=request.form.get('uname')
    upwd=request.form.get('upwd')
    return str(locals())


@app.route('/05-login',methods=['GET','POST'])
def login_views():
    #根据用户的请求方式来决定到底要做什么
    if request.method == 'GET':
    #如果是get请求的话，则响应05-login.html模板
        return render_template('05-login.html')
    else:
        #如果是post请求的话，接受请求提交的数据做进一步的处理
        uname=request.form.get("uname")
        upwd=request.form.get("upwd")
        return str(locals())


@app.route('/06-file',methods=['GET','POST'])
def file_views():
    if request.method == "GET":
        return render_template('06-file.html')
    else:
        #1、从缓存区得到上传的文件
        f = request.files['pic']
        #2、再将文件按照原始的名称保存进static目录
        f.save("static/"+f.filename)
        return "文件上传成功"

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')