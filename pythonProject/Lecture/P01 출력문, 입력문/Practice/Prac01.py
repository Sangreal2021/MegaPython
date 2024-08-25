'''
Q) 출력문을 통해 다음처럼 자기소개를 나타내보자.

- 실행화면 -
이름 : 최현
나이 : 50
번호 : 010-1234-5678
멘트 : "배고프다"

'''
#Q1 : print() 4번 사용하여 내용 출력

print('이름 :', '최현')
print('나이 :', 50)
print('번호 :', '010-1234-5678')
print('멘트 :', '\"배고프다\"')


# 02: print() 1번만 사용하고 이스케이프 코드로 내용 출력

name = '최현'
age = 50
number = '010-1234-5678'
comment = '\"배고프다\"'
print('이름 :', name, '\n', '나이 :', age, '\n', '번호 :', number, '\n', '멘트 :', comment)
print('이름 : 최현' '\n' '나이 : 50' '\n' '번호 : 010-1234-5678' '\n' '멘트 : "배고프다"')
print('이름 : 최현\n' '나이 : 50\n' '번호 : 010-1234-5678\n' '멘트 : "배고프다"')


import datetime

dt_now = datetime.datetime.now()
print(dt_now)
print(type(dt_now))
print(dt_now.year)
print(dt_now.month)
print(dt_now.hour)
print(dt_now.minute)
print(dt_now.date())
print(type(dt_now.date()))
print()

d_today = datetime.date.today()
print(d_today)
print(type(d_today))
print()

# 반복문
x = 0
while x <= 10:
    x += 1
print(x)
print()

x = 0
for i in range(1, 100):
    x += i
print(x)
print()

# 구구단
for i in range(1,10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i * j}')
    print()








