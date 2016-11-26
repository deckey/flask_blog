from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return 'Index route'

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(debug=True)