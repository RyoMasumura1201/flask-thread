from controllers.controller import app
from workers.worker import ParentThread

if __name__ == "__main__":
    t = ParentThread()
    t.start()
    app.run()