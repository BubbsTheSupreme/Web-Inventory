from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), index=True)
    password_hash = db.Column(db.String(150))

    def change_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(50), index=True)
    model = db.Column(db.String(50), index=True)
    brand = db.Column(db.String(30), index=True)
    price = db.Column(db.Integer, index=True)
    quantity = db.Column(db.Integer, index=True)
    notes = db.Column(db.String(300))
    parts = db.relationship('Components', backref='item')

class Components(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))
    part = db.Column(db.String(50), index=True)
    model = db.Column(db.String(50), index=True)
    brand = db.Column(db.String(50), index=True)
    quantity = db.Column(db.Integer, index=True)
    price = db.Column(db.Integer, index=True)

@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))