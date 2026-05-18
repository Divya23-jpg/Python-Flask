from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length


class RegistrationForm(FlaskForm):
    # ! Without custom message Error 
    # name=StringField("Full Name: ", validators=[DataRequired()])
    # ! for display custom Error  mesaage
    name=StringField("Full Name: ", validators=[DataRequired(message="We Need your name")])
    email=StringField("Email: ", validators=[DataRequired(),Email()])
    password=PasswordField("Password: ", validators=[DataRequired(),Length(min=6)])
    submit=SubmitField("Register")
    