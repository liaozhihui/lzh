# coding=utf-8
from flask import Flask,render_template

app=Flask(__name__)

@app.route("/index")
@app.route("/")
@app.route("/index/<int:num>")
@app.route("/<int:num>")
def cal(num=1):

   return "您要看第%d页"%num
@app.route("/mytemp")
def mytemp():
    str=render_template("index.html")
    print(str)
    return str
if __name__=="__main__":
    app.run(debug=True)