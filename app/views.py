from app import app

from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/about')
def about():
    return "<div style='color': blue  > Hi, Elijah here! </div>"

@app.route("/<user>")
def greet(user):
    print(f"Hi {user}!")
    return f"<h3> Hello {user} </h3>"

@app.route("/account")
def account():
    return redirect(url_for("index"))

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    
    if request.method == "POST":
        req = request.form
        
        username = req["username"]
        password = req.get("password")
        email = request.form["email"]

        print("Hello ",username, " ",password, " seems pretty unique, you'll get an email at ", email)

    return render_template("public/sign_up.html")