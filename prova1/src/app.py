from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedidos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido = db.Column(db.String(128), nullable=False)
    descricao = db.Column(db.String(256), nullable=True)
    atendido = db.Column(db.Boolean, default=False)

    def to_json(self):
        return {
            'id': self.id,
            'pedido': self.pedido,
            'descricao': self.descricao,
            'atendido': self.atendido
        }

users = {
    'user': generate_password_hash('1234'),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username], password):
        return username
    
@app.route('/')
def hello_world():
    return 'Olá! Acesse o entrypoint /novo para realizar a autenticação de usuário e realizar um novo pedido, /pedidos para consultar os pedidos cadastrados no sistema e /pedidos/{id} para consultar as informações relacionadas a um pedido específico.'

@app.route('/pedidos', methods=['GET'])
@auth.login_required
def get_pedidos():
    pedidos = Pedido.query.all()
    return jsonify({'pedidos': [pedido.to_json() for pedido in pedidos]})

@app.route('/pedidos/<int:pedido_id>', methods=['GET'])
@auth.login_required
def get_pedido(pedido_id):
    pedido = Pedido.query.get(pedido_id)
    if pedido:
        return jsonify(pedido.to_json())
    else:
        abort(404, descricao="Solicitação não encontrada.")

@app.route('/novo', methods=['POST'])
@auth.login_required
def create_pedido():
    if not request.json or not 'pedido' in request.json:
        abort(400, descricao="Bad request. 'pedido' is required.")
    pedido = Pedido(
        pedido=request.json['pedido'],
        descricao=request.json.get('descricao', ""),
        atendido=False
    )
    db.session.add(pedido)
    db.session.commit()
    return jsonify(pedido.to_json()), 201

@app.route('/pedidos/<int:pedido_id>', methods=['PUT'])
@auth.login_required
def update_pedido(pedido_id):
    pedido = db.session.get(Pedido, pedido_id)
    if not pedido:
        abort(404, descricao="Solicitação não encontrada.")
    if not request.json:
        abort(400, descricao="Bad request")
    
    pedido.pedido = request.json.get('pedido', pedido.pedido)
    pedido.descricao = request.json.get('descricao', pedido.descricao)
    pedido.atendido = request.json.get('atendido', pedido.atendido)
    db.session.commit()
    return jsonify(pedido.to_json())

@app.route('/pedidos/<int:pedido_id>', methods=['DELETE'])
@auth.login_required
def delete_pedido(pedido_id):
    pedido = db.session.get(Pedido, pedido_id)
    if not pedido:
        abort(404, descricao="Solicitação não encontrada.")
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
