from app import app

@app.route('/*')
def index():
    return "<h1>Hi, Dad</h1>"

@app.route('/about')
def about():
    return "<div style='color': blue  > Hi, Elijah here! </div>"
