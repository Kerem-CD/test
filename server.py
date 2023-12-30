import account
import calculator
from flask import Flask, redirect, render_template, request, send_file
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("loginorsign.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if account.name_check(username):
            account.signup(username, password)
            token = account.gettoken(username, password)
            return redirect("/accountprofile/" + token)
        else:
            redirect("/signup")
    return render_template("signup.html")
@app.route("/script/<name>", methods=["GET"])
def script(name):
    try:

        return send_file(f"scripts/{name}")
    except:
        return ""
@app.route("/accountprofile/<token>", methods=["GET", "POST"])
def accountprofile(token):
        
    if request.method == "POST":
        request.files["image"].save("profiles/" + account.getdatatoken(token)[0] + ".png")
        return redirect("/home/"+token)
    else:
        if token:
            return render_template("accountprofile.html")
        else:
            return redirect("/login")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if account.login(username, password):
            token = account.gettoken(username, password)
            return redirect("/home/" + token)
        else:
            return redirect("/login")
    return render_template("login.html")
@app.route("/home/<token>")
def home(token):
    if account.getdatatoken(token)!=False:
        return render_template("home.html", token=token, name=account.getdatatoken(token)[0])
    else:
        return redirect("/login")
@app.route("/getmessage/<token>")
def getmessage(token):
    if account.getdatatoken(token)!=False:
        return send_file("post.json")
    else:
        return "[]"
@app.route("/addmessage/<token>", methods=["GET"])
def addmessage(token):
    if account.getdatatoken(token)!=False:
        message = request.args.get("message")
        account.addmessage(token, message)
        return send_file("post.json")
    else:
        return "[]"
@app.route("/profilepic/<token>/<name>")
def profilepic(token, name):
    if account.getdatatoken(token)!=False:
        return send_file("profiles/" + name + ".png")
    else:
        return "[]"
app.run(debug=True, host="0.0.0.0",port=8080)
