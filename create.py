from application import app, db
from application.models import ToDos

db.drop_all()
db.create_all()

sample_todo = ToDos(
    task="Sample ToDo", 
    completed=False
    )

db.session.add(sample_todo)
db.session.commit()