from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
 return "<p>Hello </p>"


@app.route("/ram")
def sample():
 return "<p>Hello Sita</p>"

