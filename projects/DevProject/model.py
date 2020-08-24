from app import app, db


class Archers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    archer_class = db.Column(db.String(50), index = True, unique = True)
    race = db.Column(db.String(20), index = True, unique = False)
    armor = db.Column(db.String(20), index = True, unique = False)
    weapon = db.Column(db.String(20), index = True, unique = False)
    role = db.Column(db.String(30), index = True, unique = False)
    description = db.Column(db.String(400), index = True, unique = False)

    def __repr__(self):
        return f'Class {self.archer_class} main role {self.role}'

db.create_all()