from flask import Flask,make_response
from tasks.parentThread import q,queueItemList
import random
import multiprocessing
from tasks.parentThread import Status

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/start")
def start():
    item = QueueItem()
    q.put(item)
    queueItemList.append(item)
    return make_response(f'{item.name}の処理を受け付けました\n'), 202

@app.route("/cancel/<jobId>")
def cancel(jobId):
    # [TODO]queueからitemを探し、ステータス更新

    # 実行中の場合は、processを削除
    
    for childrenProcess in multiprocessing.active_children():
        if childrenProcess.name == jobId:
            childrenProcess.terminate()
    return make_response('キャンセルしました\n'), 202

class QueueItem:
    def __init__(self):
        self.name = 'item'+ str(random.random())
        self.status = Status.PENDING