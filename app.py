from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/detalhe1")
def detalhe1():
    return render_template("detalhe1.html")

@app.route("/detalhe2")
def detalhe2():
    return render_template("detalhe2.html")

@app.route("/detalhe3")
def detalhe3():
    return render_template("detalhe3.html")
