from controllers.controller import app
from workers.worker import ParentThread
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://******:******@localhost/jobdemo"
db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    status = db.Column(db.String(64))

if __name__ == "__main__":
    t = ParentThread()
    t.start()
    app.run()