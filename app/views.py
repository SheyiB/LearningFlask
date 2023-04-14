from app import app

from flask import make_response, render_template, request, redirect, url_for, session
from datetime import timedelta

app.secret_key = "demoFlask"
app.permanent_session_lifetime = timedelta(minutes=60)

@app.route('/')
def index():
    return render_template("public/index.html")


@app.route('/user')
def user():
    if 'user' in session:
        user = session["user"].get("username") 
        return render_template("public/user.html", content=user)
    else:
        return redirect(url_for('account'))

@app.route('/about')
def about():
    return "<div style='color': blue  > Hi, Elijah here! </div>"

@app.route("/greetuser/<user>")
def greet(user):
    print(f"Hi {user}!")
    #return f"<h3> Hello {user} </h3>"
    resp = make_response( render_template("public/greet.html", content=user), 201)
    resp.set_cookie('username', 'joski')
    return resp


@app.route("/login", methods = ["POST","GET"])
def account():
    if request.method == "POST":
        request.cookies.get('Me')
        session.permanent = True
        session["user"] = request.form
        return redirect(url_for("user"))
    else:
        return render_template("public/login.html")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('account'))

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        req = request.form
        username = req["username"]
        password = req.get("password")
        email = request.form["email"]
        print("Hello ",username, " ",password, " seems pretty unique, you'll get an email at ", email)
        return redirect(url_for("account"))
    else:
        return render_template("public/sign_up.html")                       