from app import app, db
from flask import render_template, request, redirect
from model import Clients, Company, Order, Products
from forms import RegistrationForm


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        client = Clients(name = reg_form.username.data, email = reg_form.email.data)
        client.set_password(reg_form.password.data)
        db.session.add(client)
        try:
            db.session.commit()
            return redirect('/success')
        except Exception:
            db.session.rollback()
            return '''<h2>This user or email already registered</h2>
            <a href="/register">Return</a>'''
        
         
    return render_template('registration.html', template_form = reg_form)
