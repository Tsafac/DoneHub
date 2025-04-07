from flask import Flask, request, jsonify
from models import Task
from db import db
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:secret@localhost/todo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'content': t.content, 'done': t.done} for t in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(content=data['content'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Tâche ajoutée'}), 201

@app.route('/tasks/<int:task_id>/done', methods=['PUT'])
def mark_done(task_id):
    task = Task.query.get(task_id)
    if task:
        task.done = True
        db.session.commit()
        return jsonify({'message': 'Tâche marquée comme terminée'})
    return jsonify({'message': 'Tâche non trouvée'}), 404

if __name__ == '__main__':
    app.run(debug=True)
