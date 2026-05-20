"""
Model:
# ? It is a python class that define database table
# ? class -> table and variable -> column

DataTypes:
# ? Defines the datatype of the databse tables(rows and column)

Relationships:
# ? it defines how the multiple data will links to each other
"""


from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

# To create all tables in the databse
db.create_all()


# ! Model-> table and Column-> column
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.string(200),unique=True)
    posts=db.relationship('Post',backref='author',lazy=True)
    # Lazy=True for relationship when u want to fetch related data


User.query.all()