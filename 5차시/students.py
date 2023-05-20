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
