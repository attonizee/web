from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from data import archers


app = Flask(__name__)
app.config['SECRET_KEY'] = 'xoo2Eim1'


@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html', archers=archers)