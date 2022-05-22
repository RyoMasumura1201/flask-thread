import threading
import time
import datetime
import queue

q = queue.Queue()

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
    
    def run(self):
        while True:
            print("workerが立ち上がりました")
            item = q.get()
            try:
                print(f'{item}が開始しました')
                for i in range(100):
                    print(f'{datetime.datetime.now():%H:%M:%S}')
                    time.sleep(1)

            finally:
                print('完了しました')
                q.task_done()