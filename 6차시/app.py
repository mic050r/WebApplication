from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def init_def():
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS tasks
    (id INTEGER PRIMARY KEY, task TEXT)"""
    )
    connection.commit()  # 저장
    connection.close()  # 종료


@app.route("/")
def index():
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FRMO tasks")
    tasks = cursor.fetchall()

    return render_template("index.html", tasks=tasks)
