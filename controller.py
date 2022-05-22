from unicodedata import name
from flask import Flask,make_response
from tasks.parentThread import q
app = Flask(__name__)

jobs={}

@app.route("/")
def hello():
    return "Hello World"

@app.route("/start/<jobId>")
def start(jobId):
    q.put(jobId)
    return make_response(f'{jobId}の処理を受け付けました\n'), 202