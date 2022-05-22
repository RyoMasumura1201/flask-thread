from flask import Flask,make_response
from tasks.parentThread import q,queueItemList
from enum import Enum
import random
import multiprocessing

app = Flask(__name__)



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
    multiprocessing.active_children()[0].terminate()
    return make_response('キャンセルしました\n'), 202

class queueItem:
    def __init__(self):
        self.name = 'item'+ str(random.random())
        self.status = status.PENDING
        
class status(Enum):
    PENDING = "pending"
    STARTED = "started"
    FINISHED = "finished"
    CANCELED = "canceled"