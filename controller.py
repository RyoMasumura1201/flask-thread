from unicodedata import name
from flask import Flask,make_response
from tasks.testThread import MyThread
app = Flask(__name__)

jobs={}

@app.route("/")
def hello():
    return "Hello World"

@app.route("/start/<threadName>")
def start(threadName):
    t = MyThread(name = threadName)
    t.start()
    jobs[threadName] = t
    return make_response(f'{threadName}の処理を受け付けました\n'), 202