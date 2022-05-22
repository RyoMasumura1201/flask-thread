import threading
import time
import datetime
import queue
from tasks.childProcess import childProcess

q = queue.Queue()

class ParentThread(threading.Thread):
    def __init__(self):
        super(ParentThread, self).__init__()
    
    def run(self):
        print("workerが立ち上がりました")
        while True:
            item = q.get()
            print(item)
            
            try:
                childP = childProcess(name=item.name)
                childP.start()

            finally:
                print('完了しました')
                q.task_done()
    
    