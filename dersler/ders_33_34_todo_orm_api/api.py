from flask import Flask, redirect, url_for, request
import utils
import json

app = Flask(__name__)

@app.route('/get_all_todos', methods=["GET"])
def get_all_todos():
    results = utils.select_todos()
    print(results)
    return json.dumps(results, indent=4)

@app.route('/create_todo', methods=["POST"])
def create_todo():
    title = request.form["title"]
    description = request.form.get("description", None)
    deadline = request.form["deadline"]
    utils.create_todo(title, deadline, description)

    results = utils.select_todos()
    return json.dumps(results, indent=4)

@app.route('/done_todo/<int:id>', methods=["GET"])
def done_todo(id):
    utils.update_todo(id)
    
    results = utils.select_todos()
    return json.dumps(results, indent=4)

if __name__ == '__main__':
    utils.create_db_and_tables()
    app.run(debug = True)