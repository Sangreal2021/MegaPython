'''
# 타입 변환(Type Casting)
'타입 변환' = '캐스팅' = '형변환'
    - 변환할 타입(데이터)
'''

# 정수형 <- 실수형
num1 = int(3.14)
print('실수를 정수로 변환:', num1, type(num1))
# 타입 변환시 데이터 값도 함께 변경됨을 주의!! (소수점 절삭)
print()

# 실수형 <- 정수형
num2 = float(50)
print(f'''정수를 실수로 변환: {num2} {type(num2)}
''')

# 문자열 <- 실수형
msg = str(10.5)
print(f'''실수를 문자열로 변환: {msg} {type(msg)}
''')

# 정수형 <- 문자열 (에러 발생)
# num0 = int('아메리카노')
# print(f'''# 문자열을 정수형으로 변환: {num0} {type(num0)}
# ''')

# 정수형 <- 문자열 (정수만 포함되어야 가능)
num3 = int('0401')
print(f'''문자열을 정수로 변환: {num3} {type(num3)}
''')

# 정수와 실수, 문자열의 연산
a = 10      # 정수
b = 25.0    # 실수
c = '100'   # 문자열

# a + b
print(a + b)    # 정수 + 실수 => 실수
print(int(a+b))
print(str(a) + str(b)) # 문자열끼리 이어붙임

# b + c
# print(b+c) # 에러
print(b + float(c))
print(int(int(c)/b))
print()

# 논리형으로 타입 변환
print(bool(-10)) # 0 제외 어떤 숫자든 True
print(bool(0)) # False
print(bool('건국전쟁')) # 빈문자열 제외 어떤 문자열이든 True
print(bool('')) # False

if 10: # True
    print('조건문')
# elif '': # False
#     print('False')
elif 't': # True
    print('True')
























