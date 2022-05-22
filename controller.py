from flask import Flask,make_response
from tasks.parentThread import q
from enum import Enum
import random

app = Flask(__name__)

queueItemList=[]

@app.route("/")
def hello():
    return "Hello World"

@app.route("/start")
def start():
    item = queueItem()
    q.put(item)
    queueItemList.append(item)
    return make_response(f'{item.name}の処理を受け付けました\n'), 202

@app.route("/cancel/<jobId>")
def cancel(jobId):
    # queueからitemを探し、ステータス更新

    # 実行中の場合は、processを削除
    return make_response('キャンセルしました\n'), 202

class queueItem:
    def __init__(self):
        self.name = 'item1'+ str(random.random())
        self.status = status.PENDING
        
class status(Enum):
    PENDING = "pending"
    STARTED = "started"
    FINISHED = "finished"
    CANCELED = "canceled"