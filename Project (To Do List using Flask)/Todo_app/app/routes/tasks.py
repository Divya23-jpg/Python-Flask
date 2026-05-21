from flask  import Blueprint,redirect,render_template,session,flash,url_for,request
from app import db
from app.models import Task


tasks_bp=Blueprint('tasks',__name__)

# ! View Tasks
@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    tasks=Task.query.all()
    return render_template('tasks.html',tasks=tasks)


# ! Add tasks
@tasks_bp.route('/add,',methods=["POST"])
def add_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    title=request.form.get('title')
    if title:
        new_tasks=Task(title=title,status='Pending')
        db.add(new_tasks)
        db.session.commit()
        flash("Task Added Successfully",'success')

    return redirect(url_for('tasks.view_tasks'))


# ! Show tasks Status
@tasks_bp.route('/toggle/<int:task_id>',methods=["POST"])
def toggle_status(task_id):
    task=Task.query.get(task_id)
    if task:
        if task.status=="Pending":
            task.status=="Working"

        elif task.status=="Working":
            task.status=="Done"

        else:
            task.staus=="Pending"
        db.session.commit()

    return redirect(url_for('tasks.view_tasks'))


# ! Cleared all tasks
@tasks_bp.route('/clear',methods=["POST"])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash("All Tasks Cleared!",'info')
    return redirect(url_for('tasks.view_tasks'))
