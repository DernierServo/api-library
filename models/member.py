from utils.db import db

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    address = db.Column(db.String(255))
    city_id = db.Column(db.Integer)
    email_address = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))

    def __init__(self, name, surname, address, city_id, email_address, phone_number):
        self.name = name
        self.surname = surname
        self.address = address
        self.city_id = city_id
        self.email_address = email_address
        self.phone_number = phone_number