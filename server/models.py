from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


db = SQLAlchemy()

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(10))
    password = db.Column(db.String(255))
    hardware = db.relationship('Hardware',backref='customer', lazy=True)


class Hardware(db.Model, SerializerMixin):
    __tablename__ = 'hardwares'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable=False)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.Integer)
    category = db.Column(db.String(255))


class Manufacturer(db.Model, SerializerMixin):
    __tablename__ = 'manufacturer'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(10))
    password = db.Column(db.String(255))
    hardware = db.relationship('Hardware', backref='manufacturer', lazy=True)


@validates("email")
def validate_email(self, key, value):
    if '@' not in value:
            raise ValueError("failed simple email validation")
    return value

@validates("phone")
def validate_phone(self, key, value):
    if not len(value) <= 10:
         raise ValueError("incorrect phone number")
    return value

@validates("firstname", "lastname")
def validate_name(self, key, value):
     if not len(value) <= 20:
          raise ValueError("long name")
     return value
         