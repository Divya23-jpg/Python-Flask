# Create models which means tables for database

# ! It link to db oject which makes in __init__.py(app)
from app import db

# ! table Creation named Task and col(id,title,status)
class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    status=db.Column(db.String(20), default="Pending")