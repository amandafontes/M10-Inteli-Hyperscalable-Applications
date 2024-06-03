# routes.py
from flask import Blueprint, request, jsonify
from models import db, User
from utils import generate_token

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        token = generate_token(user)
        return jsonify({'token': token})
    return jsonify({'message': 'Credenciais inválidas'}), 401

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Usuário registrado com sucesso'})
