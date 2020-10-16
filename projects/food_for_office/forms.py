from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length, Regexp


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = [InputRequired(), 
        Length(min=3, max=50, message='Minimum length must be 3 symbols and maximum 50')])
    email = StringField('Email', validators = [InputRequired(), 
        Length(max=110, message='Maximum 110 symbols'), 
        Email(message='Not email format. Must be: name@domain')])
    password = PasswordField('Password', validators = [InputRequired(), 
        Regexp('^(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).{8,32}$', 
        message='''Password minimal length 8 symbols, maximum 32 symbols. 
        Must contain at least one uppercase, lowercase letter, 
        one numeric digit.''')])
    password2 = PasswordField('Repeat Password', validators = [InputRequired(), 
        EqualTo('password', message='Passwords must much')])
    submit = SubmitField('Register')

