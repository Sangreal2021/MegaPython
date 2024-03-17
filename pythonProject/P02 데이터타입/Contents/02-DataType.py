'''
# 자료형(Data Type)
1. 정수형(int) : 음수, 0, 양수 데이터.
    - Integer
2. 실수형(float) : 소수점을 포함한 숫자 데이터.
3. 문자열(str) : 문자열 데이터.
    - String
4. 논리형(bool) : 참, 거짓을 나타내는 논리형 데이터.(대문자로 시작)
    - Boolean
'''
num1 = 10 # 정수형
num2 = 2.5 # 실수형
num2 = 10.0 # 실수형(소수점 포함)
msg = '3월' # 문자열
msg = '10' # 문자열(따옴표 포함)
flag = False # 논리형
flag = True

print(num1, type(num1))
print(num2, type(num2))
print(msg, type(msg))
print(flag, type(flag))
print()

# 같은 이름의 변수라도 대입하는 값이 바뀌면 데이터 타입도 변함.
var = 20
print('var :', var, type(var))
var = 36.5
print('var :', var, type(var))
var = 'Sunday'
print('var :', var, type(var))




















