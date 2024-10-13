from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('mongodb://localhost:27017')
db = client['python_task_management']
tasks_collection = db['tasks']

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(tasks_collection.find())
    for task in tasks:
        task['_id'] = str(task['_id'])
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task_data = request.json
    result = tasks_collection.insert_one(task_data)
    return jsonify({'_id': str(result.inserted_id)}), 201

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    task_data = request.json
    result = tasks_collection.update_one({'_id': task_id}, {'$set': task_data})
    if result.modified_count > 0:
        return jsonify({'message': 'Task updated successfully'})
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = tasks_collection.delete_one({'_id': task_id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Task deleted successfully'})
    return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
