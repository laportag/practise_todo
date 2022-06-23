from application import app, db
from application.models import ToDos
from application.forms import TaskForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def index():
    todo = ToDos.query.all()
    # todo = ToDos.query.all()
    # str = ""
    # for task in todo:
    #     str += f'{task.task} {task.completed} <br>' 
    return render_template("task.html", todos=todo)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add', methods = ['GET','POST'])
def add():
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            taskData = ToDos(
                task = form.task.data,
                completed = form.completed.data
            )
            db.session.add(taskData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addtask.html', form=form)


# @app.route('/add/<task_name>')
# def add(task_name):
#     new_task = ToDos(task=task_name)
#     db.session.add(new_task)
#     db.session.commit()
#     return new_task.task

@app.route('/complete/<task_name>')
def complete(task_name):
    task = ToDos.query.filter_by(task=task_name).first()
    task.completed = True
    db.session.commit()
    return task.task + " is complete: " + str(task.completed)

@app.route('/incomplete/<task_name>')
def incomplete(task_name):
    task = ToDos.query.filter_by(task=task_name).first()
    task.completed = False
    db.session.commit()
    return task.task + " is complete: " + str(task.completed)

@app.route('/delete/<int:id>')
def delete(id):
    todo = ToDos.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<task_name>/<new_name>')
def update(task_name, new_name):
    task = ToDos.query.filter_by(task=task_name).first()
    task.task = new_name
    db.session.commit()
    return task.task