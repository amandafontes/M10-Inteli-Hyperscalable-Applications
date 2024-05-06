from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=True)
    done = db.Column(db.Boolean, default=False)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done
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
    return 'Olá! Acesse o entrypoint /tasks para realizar a autenticação de usuário e consultar as tarefas da lista.'

@app.route('/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    tasks = Task.query.all()
    return jsonify({'tasks': [task.to_json() for task in tasks]})

@app.route('/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = Task.query.get(task_id)
    if task:
        return jsonify(task.to_json())
    else:
        abort(404, description="Task not found")

@app.route('/tasks', methods=['POST'])
@auth.login_required
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400, description="Bad request. 'title' is required.")
    task = Task(
        title=request.json['title'],
        description=request.json.get('description', ""),
        done=False
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_json()), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
@auth.login_required
def update_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        abort(404, description="Tarefa não encontrada.")
    if not request.json:
        abort(400, description="Bad request")
    
    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.done = request.json.get('done', task.done)
    db.session.commit()
    return jsonify(task.to_json())

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@auth.login_required
def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        abort(404, description="Tarefa não encontrada.")
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
