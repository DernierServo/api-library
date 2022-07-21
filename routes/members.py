from flask import Blueprint
from utils.db import db
from models.member import Member


members = Blueprint('members', __name__)

@members.route('/member', methods=['POST'])
def add_member():
    try:
        name = request.json['name']
        surname = request.json['surname']
        address = request.json['address']
        city_id = request.json['city_id']
        email_address = request.json['email_address']
        phone_number = request.json['phone_number']

        new_member = Member(name, surname, address, city_id, email_address, phone_number)
        db.session.add(new_member)
        db.session.commit()
        return jsonify({'msg': 'The member was added'})
    except:
        return jsonify({'msg': 'Error'})


@members.route('/member', methods=['GET'])
def list_members():
    members = []
    try:
        query = Member.query.all()
        for data in query:
            member = {
                'name': data.name,
                'surname': data.surname,
                'address': data.address,
                'email_address': data.email_address,
                'phone_number': data.phone_number
            }
            members.append(member)
        return jsonify({'msg': 'List of members', 'members':members})
    except:
        return jsonify({'msg': 'Error'})