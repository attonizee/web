from flask import render_template, request, redirect, flash
from app import app, db
from model import Clients, Company, Order, Products
from forms import RegistrationForm


@app.route('/')
def index():
    return '''<h2>Hello, home page</h2>
    <a href="/register">Register</a>'''


@app.route('/login')
def success():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    error = None
    if request.method == 'POST':
        if reg_form.validate_on_submit():
            client = Clients(name=reg_form.username.data, email=reg_form.email.data)
            client.set_password(reg_form.password.data)
            db.session.add(client)
            try:
                db.session.commit()
                flash('User succesfully created')
                return redirect('/login')
            except Exception:
                db.session.rollback()
                error = 'This user or email already registered'
    
    return render_template('registration.html', template_form=reg_form, error=error)
    
        
