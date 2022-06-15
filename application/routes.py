from application import app, db
from application.models import ToDos
from flask import Flask

@app.route('/')
def index():
    todo = ToDos.query.first()
    return todo.task

@app.route('/add')
def add():
    return "added new todo"
