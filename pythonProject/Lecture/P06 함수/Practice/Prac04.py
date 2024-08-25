'''
Q)  사용자로부터 두 개의 정수를 입력받고,
    4개의 함수 중에서 선택하여 실행시켜
    두 수의 연산 결과를 나타내시오.
    함수명: add, sub, mul, div
    매개변수: 정수형 2개
    리턴값: 정수형 1개

   ↓ 실행화면1 ↓
    정수1 입력: 10
    정수2 입력: 20
    ---------------
    두 수의 연산 선택
    1. 합
    2. 차
    3. 곱
    4. 나눗셈
    ---------------
    연산을 선택하시오: 1
    연산 결과: 30

    ↓ 실행화면2 ↓
    정수1 입력: 10
    정수2 입력: 20
    ---------------
    두 수의 연산 선택
    1. 합
    2. 차
    3. 곱
    4. 나눗셈
    ---------------
    연산을 선택하시오: 3
    연산 결과: 200
'''
def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b
def div(a, b): return a/b

num1 = int(input('정수1 입력: '))
num2 = int(input('정수2 입력: '))
print(f'''-------------------
두 수의 연산 선택
1. 합
2. 차
3. 곱
4. 나눗셈
-------------------''')
menu = int(input('연산을 선택하시오: '))
if menu == 1:
    result = add(num1, num2)
elif menu == 2:
    result = sub(num1, num2)
elif menu == 3:
    result = mul(num1, num2)
elif menu == 4:
    result = div(num1, num2)

# print('연산 결과:', result)


# 심화) 딕셔너리를 이용하여 함수 선택하기
# 임시로 내장함수명 변경 가능 (p = print)
select = {1:add, 2:sub, 3:mul, 4:div}
f = select[menu]
print('연산 결과:', f(num1, num2))



















