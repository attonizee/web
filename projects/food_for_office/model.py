from app import app, db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Clients(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    registration_date = db.Column(db.DateTime(), index = True, default=datetime.utcnow)
    company = db.relationship('Company', backref = 'clients', lazy = 'dynamic')
    order = db.relationship('Order', backref = 'clients', lazy = 'dynamic')

    def __repr__(self):
        return f'User name {self.name} has email {self.email} and registered at {self.registration_date}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    address = db.Column(db.String(120), index = True, unique = False)
    user_id = db.Column(db.Integer, db.ForeignKey('clients.id'))

    def __repr__(self):
        return f'Company {self.name} located {self.address}'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    products_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('clients.id'))

    def __repr__(self):
        return f'User {self.user_id} ordered {self.products_id} in amount of {self.amount}'


class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), index = True, unique = True)

    def __repr__(self):
        return f'Product {self.name}'


if __name__ == '__main__':
    db.create_all()