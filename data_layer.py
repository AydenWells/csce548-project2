import sqlite3

DB_NAME = "project2.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# CRUD
def create_student(name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO student (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def get_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM student WHERE id = ?", (student_id,))
    row = cur.fetchone()
    conn.close()
    if row is None:
        return None
    return {"id": row[0], "name": row[1], "email": row[2]}


def update_student(student_id, name, email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE student SET name = ?, email = ? WHERE id = ?",
        (name, email, student_id),
    )
    conn.commit()
    changed = cur.rowcount
    conn.close()
    return changed > 0


def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE id = ?", (student_id,))
    conn.commit()
    changed = cur.rowcount
    conn.close()
    return changed > 0