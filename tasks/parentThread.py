import threading
import queue
import time
import datetime
import multiprocessing
from enum import Enum

q = queue.Queue()
queueItemList=[]

class ParentThread(threading.Thread):
    def __init__(self):
        super(ParentThread, self).__init__()
    
    def run(self):
        print("workerが立ち上がりました")
        while True:
            item = q.get()
            
            try:
                itemInList = list(filter(lambda x: x.name == item.name, queueItemList))[0]
                if itemInList.status == Status.PENDING:
                    #[TODO] status更新
                    childP = childProcess(name=item.name)
                    childP.start()
                    childP.join()

            finally:
                print('parent完了しました')
                q.task_done()
                
class childProcess(multiprocessing.Process):
    def __init__(self,name):
        super(childProcess, self).__init__()
        self.name = name
    
    def run(self):
        print("childworkerが立ち上がりました")    
        try:
            print(f'{self.name}が開始しました')
            for i in range(30):
                print(f'{datetime.datetime.now():%H:%M:%S}')
                time.sleep(1)

        finally:
            print('childThreadが完了しました')

class Status(Enum):
    PENDING = "pending"
    STARTED = "started"
    FINISHED = "finished"
    CANCELED = "canceled"
    