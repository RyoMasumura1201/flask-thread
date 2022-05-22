from controller import app
from tasks.testThread import MyThread,q


if __name__ == "__main__":
    t = MyThread()
    t.start()
    app.run()