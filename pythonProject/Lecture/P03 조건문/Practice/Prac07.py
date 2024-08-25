'''
Q)  사용자로부터 세 개의 숫자를 입력 받은 후
    가장 큰 숫자를 출력하라.

    ↓ 실행화면 ↓
    input number1: 10
    input number2: 9
    input number3: 20
    가장 큰 수: 20
'''

num1 = int(input('input number1: '))
num2 = int(input('input number2: '))
num3 = int(input('input number3: '))

# 중첩문 사용
# if num1 >= num2:
#     if num1 >= num3:
#         print('가장 큰 수: ', num1)
#     else:
#         print('가장 큰 수: ', num3)
# else:
#     if num2 >= num3:
#         print('가장 큰 수: ', num2)
#     else:
#         print('가장 큰 수: ', num3)

# 논리연산자 사용
# if num1 >= num2 and num1 >= num3:
#     print('가장 큰 수: ', num1)
# elif num2 >= num3:
#     print('가장 큰 수: ', num2)
# else:
#     print('가장 큰 수: ', num3)

# 최대값을 저장할 변수 도입 (가장 합리적인 방법!!)
max = num1 # 첫번째 변수로 시작
if num2 > max:
    max = num2
if num3 > max:
    max = num3

print('가장 큰 수:', max)













