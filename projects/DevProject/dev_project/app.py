from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from data import l2_classes


app = Flask(__name__)
app.config['SECRET_KEY'] = 'xoo2Eim1'


@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html', l2_classes=l2_classes)

@app.route('/classes/<l2_class>')
def classes(l2_class):
    return render_template('classes.html', template_class_name = l2_class, template_l2_class = l2_classes[l2_class])