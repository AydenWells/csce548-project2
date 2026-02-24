import data_layer


def setup():
    data_layer.init_db()


def add_student(name, email):
    # simple “business rule”: basic validation
    if not name or not email:
        raise ValueError("Name and email are required.")
    return data_layer.create_student(name, email)


def fetch_student(student_id):
    return data_layer.get_student(student_id)


def modify_student(student_id, name, email):
    if student_id <= 0:
        raise ValueError("Student id must be positive.")
    return data_layer.update_student(student_id, name, email)


def remove_student(student_id):
    return data_layer.delete_student(student_id)