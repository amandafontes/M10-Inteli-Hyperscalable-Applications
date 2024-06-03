from flask import Blueprint, request, jsonify
from models import db, MainData

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET'])
def get_main_data():
    data = MainData.query.all()
    return jsonify([d.to_dict() for d in data])

@main_blueprint.route('/', methods=['POST'])
def add_main_data():
    data = request.get_json()
    new_data = MainData(attribute=data['attribute'])
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict())
