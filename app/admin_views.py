from app import app

@app.route('/admin/dashboard')
def admin_dashboard():
    return "<h1>Hi, Admin Here</h1>"

@app.route('/admin/profile')
def admin_profile():
    return "<h1 style='color': blue  > Hi, Elijah the Admin here! </h1>"
