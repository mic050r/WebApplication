import sqlite3


def create_table():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS students
                        (id INTEGER PRIMARY KEY, name TEXT, 
                        age INTEGER, major TEXT)"""
    )

    connection.commit()
    connection.close()


create_table()


def insert_student(name, age, major):
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO students(name, age, major)
    VALUSE (?,?,?)""",
        (name, age, major),
    )
    connection.commit()
    connection.close()


# insert_student("john", 21, "computer science")


def query_student():
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    connection.close()
    return rows


print(query_student())
