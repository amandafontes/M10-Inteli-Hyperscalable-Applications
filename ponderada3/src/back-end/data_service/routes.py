from flask import Blueprint, request, jsonify
from models import db, Data

data_blueprint = Blueprint('data', __name__)

@data_blueprint.route('/', methods=['GET'])
def get_data():
    data = Data.query.all()
    return jsonify([d.to_dict() for d in data])

@data_blueprint.route('/', methods=['POST'])
def add_data():
    data = request.get_json()
    new_data = Data(name=data['name'], value=data['value'])
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict())
