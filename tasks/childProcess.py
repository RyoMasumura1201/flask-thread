import threading
import time
import datetime
import multiprocessing

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
