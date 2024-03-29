'''
# 출력문
print(출력할 내용)
print(내용1, 내용2, 내용3, ...)
'''

# 숫자 출력 print(숫자)
print(401) # 정수 출력
print(36.5) # 실수 출력
print()

# 문자열 출력 print('문자열')
print('401호 강의실' + '\n' + 'Java')
print("401호 강의실")
print('# 401호' + '\n')

# 여러 개의 문자열 출력
print('2024년', '청룡의', '해') # 콤마(,)로 이어 붙이면 공백 포함
print('2024년', 15)
print('2024년' + '청룡의' + '해') #덧셈기호(+)로 이어 붙이면 공백X
print('2024년' '청룡의' '해')

# 여러 데이터 타입을 혼합해서 출력
print(1, '더하기', 2, '는', 1+2)
print(1, '+', 2, '=', 1+2)
# print(401 + '호 강의실') # -> 에러
print(401, '호 강의실', sep='') # ','와 문자 사이의 공백 제거

a = 'Java'
b = 'Python'
c = a + b
print(c)

a = [10, 20, 30]
b = a
a[2] = 200
print(b, a)
print()

# 여러줄 텍스트 문자열 출력
print('''여러줄 텍스트 는
여러줄 의 문자열 내용을
한줄씩 띄워서 출력''')
print()

# 여러줄 텍스트로 내용출력
print('''
이름 : 최현
나이 : 50
번호 : 010-1234-5678
멘트 : "배고프다"
''')










