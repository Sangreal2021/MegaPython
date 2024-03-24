'''
# 복합 대입 연산자
+=, -=, *=, /=, %=, **=
사칙연산자 + 대입연산자
제어문(조건문, 반복문)에서 자주 사용

'''

a = 100
a += 10 # a = a + 10
print(a)

a -= 10 # a = a - 10
print(a)

a *= 5
print(a)

a //= 50
print(a)

a %= 4
print(a)

a **= 3
print(a)
print('='*20)

# += 연산
num1 = 100
num1 += 10
num1 += 20
print('num1:', num1)

# -= 연산
num2 = 30
num2 -= 30
num2 -= 30
num2 -= 30
print('num2:', num2)

# 1~10까지의 수 더하기
sum = 0
for i in range(1, 11):
    sum += i
    print(f'{i}번째 sum값: {sum}')
print('총합:', sum)

# 1~10까지 짝수들의 합 구하기
sum = 0
for i in range(1, 11):
    if i%2 == 0:
        sum += i
print(f'짝수합: {sum}')

# 1~250까지 13의 배수 개수 구하기
cnt = 0 # 개수를 셀 변수
for i in range(1, 250):
    if i%13 == 0:
        cnt += 1
print(f'13의 배수의 개수: {cnt}')














