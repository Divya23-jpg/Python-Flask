from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


def create_app():
    app=Flask(__name__)

# It sets configuration like where is databse,secret key? debugging is happening or not 
#  SQLALCHEMY_DATABASE_URI is a special key which SQLAlchemy will looks
#  URI= Uniform Resource Indentifier this says this is a database u have to use it now

# ! sqllite:///site.db:  
# ? sqllite  tells that we r using sqllite databse
# ? ///  file is in this project folder
# ? site.db is a databse file name

    app.config['SQLALCHEMY_DATABASE_URI']='sqllite:///site.db'


# ! Most Important alwaysb use
    db.init_app(app)
    return app