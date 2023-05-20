from flask import Flask

app = Flask(__name__)


def about_flask():
    return f"""
    <html>
    <body>
        <h1>About Flask</h1>
        <p>플라스크는 가벼우면서도 강력한 파이썬 웹 프레임워크입니다.</p>
        <p>플라스크의 주요 특징:</p>
        <ul>
            <li>가벼움: 필요한 기능을 선택적으로 추가할 수 있습니다.</li>
            <li>유연성: 개발자가 프로젝트에 맞게 커스터마이즈할 수 있습니다.</li>
            <li>유연함: 다양한 플라스크 확장팩(Flask extension)을 통해 데이터베이스 연동, 인증, 폼 처리 등 다양한 기능을 추가할 수 있습니다</li>
        </ul>
    </body>
    </html>
    """


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/about")
def about():
    return about_flask()


if __name__ == "__main__":
    app.run(debug=True)  # 원하는 포트 번호로 변경
