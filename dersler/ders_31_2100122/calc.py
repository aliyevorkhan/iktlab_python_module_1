from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/topla', methods=["POST"])
def topla():
    a = float(request.form["a"])
    b = float(request.form["b"])
    return str(a+b)

@app.route('/cixart', methods=["POST"])
def cixart():
    a = float(request.form["a"])
    b = float(request.form["b"])
    return str(a-b)

@app.route('/vur', methods=["POST"])
def vur():
    a = float(request.form["a"])
    b = float(request.form["b"])
    return str(a*b)

@app.route('/bol', methods=["POST"])
def bol():
    a = float(request.form["a"])
    b = float(request.form["b"])
    return str(a/b)

if __name__ == '__main__':
   app.run(debug = True)