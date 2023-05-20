# datetime 모듈을 임포트
from datetime import datetime


def current_time():
    now = datetime.now()
    time_string = now.strftime("%Y년 %m일 %d일 %H시 %M분 %S초")
    return f"현재시간 : {time_string}"


if __name__ == "__main__":
    print(current_time())
