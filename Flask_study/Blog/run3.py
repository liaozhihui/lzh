# coding=utf-8
from flask import Flask,render_template,request
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


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')