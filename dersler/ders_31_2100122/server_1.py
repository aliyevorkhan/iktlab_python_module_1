from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/g', methods=["GET"])
def get_req():
    result = request.url.split("?")[-1].split("&")

    return str(result)

@app.route('/p', methods=["POST"])
def post_req():
   return 'POST request atildi'

@app.route('/g_p', methods=["GET", "POST"])
def get_post_req():
    if request.method == "GET":
        return 'GET request atildi'
    elif request.method == "POST":
        username = request.form["uname"]
        password = request.form["pwd"]
        if username == "admin" and password == "1234":
            return "Admin oldugunuz tesdiqlendi" + str(request.url)
        else:
            return "Admin Deyilsiniz!"
            
if __name__ == '__main__':
   app.run(debug = True)