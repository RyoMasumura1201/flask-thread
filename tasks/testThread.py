import threading
import time
import datetime
class MyThread(threading.Thread):
    def __init__(self,name):
        super(MyThread, self).__init__()
        self.name = name
        self.stop_event = threading.Event()
    
    def stop(self):
        self.stop_event.set()
    
    def run(self):
        try:
            print(f'{self.name}が開始しました')
            for i in range(100):
                print(f'{datetime.datetime.now():%H:%M:%S}')
                time.sleep(1)

                if self.stop_event.is_set():
                    break
        finally:
            print('完了しました')