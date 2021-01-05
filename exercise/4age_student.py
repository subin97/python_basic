from datetime import datetime as dt

current_year = dt.today().year
print("태어난 년도를 입력하세요: ", end='')
birth_year = int(input())
age = current_year - birth_year + 1

if age>=17 and age<20:
    print('고등학생 입니다.')
elif age>=20 and age<27:
    print('대학생 입니다.')
else:
    print('학생이 아닙니다.')