from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [InputRequired()])
    email = StringField('Email', validators = [InputRequired(), Email(message='Not email format name@domain')])
    password = PasswordField('Password', validators = [InputRequired()])
    password2 = PasswordField('Repeat Password', validators = [InputRequired(), EqualTo('password', message='Passwords must much')])
    submit = SubmitField('Register')

