from application import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(60))
    completed = db.Column(db.Boolean, default=False)