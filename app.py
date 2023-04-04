from flask import Flask

app = Flask(__name__)

@app.route('/*')
def index():
    return "<h1>Hi, Dad</h1>"

@app.route('/about')
def about():
    return "<div style='color': blue; 'background': black;  > Hi, Elijah here! </div>"

if __name__ == "__main__":
    app.run()