import data_layer


def setup():
    data_layer.init_db()


def add_student(name, email):
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


# -------- Project 3 additions below --------

def fetch_all_students():
    return data_layer.get_all_students()


def fetch_students_by_name(name_substring):
    if name_substring is None:
        name_substring = ""
    return data_layer.search_students_by_name(name_substring)