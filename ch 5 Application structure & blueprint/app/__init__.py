"""
!This file says There is no empty file here, 

! Its module where we can import our neccessary module"""


from flask import Flask
from routes.auth import auth_bp #its Login blueprint

def create_app():
    app=Flask(__name__)
    app.secret_key="my-secret-key"
    app.register_blueprint(auth_bp)
    return app