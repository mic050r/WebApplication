# Flask와 SQLite 모듈을 불러오는 부분
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Flask 인스턴스를 생성하고 'app'변수에 할당
app = Flask(__name__)


# init_def 함수를 정의 하여 데이터 베이스를 초기화
def init_db():
    # 작업을 저장할 'task' 테이블을 생성
    connection = sqlite3.connect("example.db")  # example.db 파일과 연결을 생성
    cursor = connection.cursor()  # cursor 객체 생성
    cursor.execute(  # cursor에 테이블을 만드는 SQL구문을 주입
        """CREATE TABLE IF NOT EXISTS tasks
    (id INTEGER PRIMARY KEY, task TEXT)"""
    )
    connection.commit()  # 변경사항을 저장
    connection.close()  # 연결 종료


# 루트페이지('/')를 처리하기 위해, 'index'함수를 정의
# '@app.route('/') 데코레이저를 사용하여 이 함수를 루트 url에 연결
@app.route("/")
# 데이터베이스에서 작업 목록을 가져와 'index.html' 템플릿에 전달
def index():
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FRMO tasks")
    tasks = cursor.fetchall()
    # templates 폴더에 저장된 index.html을 불러오는 부분
    return render_template("index.html", tasks=tasks)


# 작업을 추가하기 위한 'add_taxk'함수를 정의
@app.route("/add", methods=["POST"])  # 이 함수를 '/add' URL에 연결
def add_task():
    # <form> 태그에서 보낸 작업명을 task 변수에 저장하는 코드
    task = request.form["task"]
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    connection.commit()
    connection.close()
    # index 함수로 연결해주는 부분
    return redirect(url_for("index"))


# 작업을 삭제하기 위한 'delete_task'함수를 정의
@app.route("/delete/<int:task_id>")  # <a> 태그의 task[0] 값을 정수형 변수 task_id의 인자로 받아오는 부분
def delete_task(task_id):
    # 작업 ID를 인자로 받아 해당 작업을 데이터베이스에서 삭제
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    connection.commit()
    connection.close()
    # 루트 페이지로 리디렉션 => index 함수로 연결해주는 부분
    return redirect(url_for("index"))


# 메인함수 생성
# 데이터 베이스를 연결하기 위한 함수인 init_db()를 호출
# flask를 실행하기 위한 함수인 app.run()함수를 호출
# run함수 안에 인자값으로 debug=True옵션을 주면 터미널에서 애플리케이션이 동작하는 과정을 확인 가능
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
