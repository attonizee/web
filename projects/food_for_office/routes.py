from app import app, db
from flask import render_template, request
from model import Clients, Company, Order, Products
from forms import RegistrationForm


@app.route('/newuser')
def new_user():
    reg_form = RegistrationForm()
    return render_template('registration.html', template_form = reg_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        client = Clients(name = reg_form.username.data, email = reg_form.email.data)
        client.set_password(reg_form.password.data)
        db.session.add(client)
        try:
            db.session.commit()
            return render_template('registered.html',template_user = client )
        except Exception:
            db.session.rollback()
            print('Something wrong')
            return '<h2>This user already exist</h2>'
    
