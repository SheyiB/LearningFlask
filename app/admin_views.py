from app import app

from flask import render_template

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route('/admin/profile')
def admin_profile():
    return "<h1 style='color': blue  > Hi, Elijah the Admin here! </h1>"
