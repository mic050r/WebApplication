# datetime 모듈을 임포트
from datetime import datetime

# 현재 시간을 출력하는 함수인 now를 변수 now에 할당
now = datetime.now()
# 원하는 형식으로 시간을 출력할 수 있는 strftime을 이용하여 익숙한 형태의 문자열로 변환
time_string = now.strftime("%Y년 %m일 %d일 %H시 %M분 %S초")
# 문자열 포멧팅을 이용하여 현재시간을 출력하는 문자열에 현재시간을 할당하여 print함수로 출력
print(f"현재시간 : {time_string}")
