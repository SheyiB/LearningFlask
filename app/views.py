from app import app

from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return "<div style='color': blue  > Hi, Elijah here! </div>"
