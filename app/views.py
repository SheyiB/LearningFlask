from app import app

from flask import render_template, request, redirect, url_for, session

app.secret_key = "demoFlask"

@app.route('/')
def index():
    return render_template("public/index.html")


@app.route('/user')
def user():
    user = session["user"].get("username") 
   
    return render_template("public/user.html", content=user)

@app.route('/about')
def about():
    return "<div style='color': blue  > Hi, Elijah here! </div>"

@app.route("/greetuser/<user>")
def greet(user):
    print(f"Hi {user}!")
    #return f"<h3> Hello {user} </h3>"
    return render_template("public/greet.html", content=user)

@app.route("/login", methods = ["POST","GET"])
def account():
    if request.method == "POST":
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