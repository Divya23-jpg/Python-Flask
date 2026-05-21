from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ! Create databse object globally
db=SQLAlchemy()

def create_app():

    app=Flask(__name__)
    # secret key for security 
    app.config['SECRET_KEY']='your-secret-key'
    # Where is database? its in todo.db
    app.config['SQLALCHEMY_DATABASE_URI']='sqllite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

    # link db to app
    db.__init__(app)

    # ! Create blueprint
    from app.routes.auth import auth_bp
    from app.routes.auth import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    
    return app