import threading
import queue
import time
import datetime
import multiprocessing
from enum import Enum

q = queue.Queue()

class ParentThread(threading.Thread):
    def __init__(self):
        super(ParentThread, self).__init__()

    def run(self):
        while True:
            item = q.get()

            try:
                from util.db_config import Task, db
                task = Task.query.filter_by(id=item.id).first()
                if task.status == Status.PENDING:
                    task.status = Status.STARTED.value
                    db.session.add(task)
                    db.session.commit()
                    childP = childProcess(name=item.name)
                    childP.start()
                    childP.join()

                    if task.status == Status.STARTED.value:
                        task.status = Status.COMPLETED.value
                        db.session.add(task)
                        db.session.commit()

            finally:
                q.task_done()

class childProcess(multiprocessing.Process):
    def __init__(self,name):
        super(childProcess, self).__init__()
        self.name = name

    # 処理内容
    def run(self):
        try:
            print(f'{self.name}が開始しました')
            for i in range(30):
                print(f'{datetime.datetime.now():%H:%M:%S}')
                time.sleep(1)

        finally:
            print(f'{self.name}が終了しました')

class Status(Enum):
    PENDING = "pending"
    STARTED = "started"
    FINISHED = "finished"
    CANCELED = "canceled"