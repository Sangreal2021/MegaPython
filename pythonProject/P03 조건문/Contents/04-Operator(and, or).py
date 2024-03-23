'''
# 논리연산자
and, or, not
조건식에 대한 결과를 참 또는 거짓으로 반환.

A and B : 양쪽 조건식이 둘 다 True 인 경우 => 결과도 True
A or B : 둘 중 하나의 조건식이라도 True 인 경우 => 결과도 True
not A : A의 논리값(True, False)의 반대 결과 반환

'''

num1 = 50
num2 = 20
num3 = 10
print('and 예시1:', num1>30 and num2>10)
print('and 예시2:', num1>30 and num2>20)
print('or 예시1:', num1>30 or num2>20)
print('or 예시2:', num1>60 or num2>30)
print('일반비교:', num1>num2>num3) # num1>num2 and num2>num3

print('not비교:', not num1>num2>num3)
print(not True, not False)

# 조건문과 논리연산자 함께 사용하기
# if A and B
math = 90 # int(input('수학 점수 >> '))
science = 80 # int(input('과학 점수 >> '))
if math >= 90 and science >= 80:
    print('공대에 합격입니다.')
else:
    print('공대에 불합격입니다.')

# if A or B
music = 90
art = 70
if music >= 90 or art >= 80:
    print('예술대에 합격입니다.')
else:
    print('예술대에 불합격입니다.')































