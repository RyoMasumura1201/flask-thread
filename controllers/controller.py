from flask import Flask,make_response
from util.env import DATABASE_PASSWORD
from workers.worker import q, Status
import random
import multiprocessing

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:"+ DATABASE_PASSWORD + "@localhost/taskdemo"

@app.route("/start")
def start():
    from util.db_config import Task, db
    item = QueueItem()
    q.put(item)

    taskForDB = Task(name = item.name, status = Status.PENDING.value)
    db.session.add(taskForDB)
    db.session.commit()
    return make_response(f'{item.name}の処理を受け付けました\n'), 202

@app.route("/cancel/<taskId>")
def cancel(taskId):
    from util.db_config import Task, db
    task = Task.query.filter_by(id=taskId).first()
    task.status = Status.CANCELED.value
    db.session.add(task)
    db.session.commit()

    # 実行中の場合は、processを削除
    for childrenProcess in multiprocessing.active_children():
        if childrenProcess.name == taskId:
            childrenProcess.terminate()
    return make_response('キャンセルしました\n'), 202

class QueueItem:
    def __init__(self):
        self.name = 'item'+ str(random.random())