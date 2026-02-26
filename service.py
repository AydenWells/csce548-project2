from flask import Flask, request, jsonify
from flask_cors import CORS
import business_layer

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Hosting instructions (put this comment in your submission!)
# Run locally:
#   1) activate venv
#   2) python service.py
# Service will be hosted at:
#   http://127.0.0.1:5000


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/student", methods=["POST"])
def create_student():
    data = request.get_json(force=True)
    try:
        new_id = business_layer.add_student(data.get("name"), data.get("email"))
        return jsonify({"id": new_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/student/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = business_layer.fetch_student(student_id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200


@app.route("/student", methods=["PUT"])
def update_student():
    data = request.get_json(force=True)

    student_id = data.get("id")
    if student_id is None:
        return jsonify({"error": "Missing id"}), 400

    try:
        student_id = int(student_id)
    except Exception:
        return jsonify({"error": "id must be a number"}), 400

    try:
        ok = business_layer.modify_student(student_id, data.get("name"), data.get("email"))
        if not ok:
            return jsonify({"error": "Student not found"}), 404
        return jsonify({"updated": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/student/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    ok = business_layer.remove_student(student_id)
    if not ok:
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"deleted": True}), 200

@app.route("/students", methods=["GET"])
def get_all_students():
    return jsonify(business_layer.fetch_all_students()), 200


@app.route("/students/search", methods=["GET"])
def search_students():
    q = request.args.get("q", "")
    return jsonify(business_layer.fetch_students_by_name(q)), 200


if __name__ == "__main__":
    business_layer.setup()
    app.run(debug=True)