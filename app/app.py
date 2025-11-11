# app/app.py
from flask import Flask, request, jsonify, redirect, url_for
from app.services import TodoService

app = Flask(__name__)
service = TodoService()

@app.route("/")
def index():
    # Redirect root to the tasks listing to avoid 404 on "/"
    return redirect(url_for("get_tasks"))

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(service.list_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    try:
        task = service.create_task(data.get("title"))
        return jsonify(task), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/tasks/<int:task_id>/done", methods=["POST"])
def mark_done(task_id):
    try:
        task = service.mark_done(task_id)
        return jsonify(task)
    except KeyError:
        return jsonify({"error": "Not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    try:
        task = service.update_task(task_id, data.get("title"))
        return jsonify(task)
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    try:
        service.delete_task(task_id)
        return "", 204
    except KeyError:
        return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

