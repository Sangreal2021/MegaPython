# == 문자열 관련 함수 == #
a = 'My Weekend'
print(len(a))

# 문자 개수 세기
print('문자열에서 e의 개수:', a.count('e'))

# 특정 문자 위치 찾기
print('문자열에서 y의 위치:', a.index('y'))
print('문자열에서 y의 위치:', a.find('y'))

# print('문자열에 없는 문자 찾을때:', a.index('z'))    # Error
print('문자열에 없는 문자 찾을때:', a.find('z'))       # -1 반환
print('='*45)

# 공백 제거하기 - strip()
k = ' spring '
print(f'원본: ({k})')
print(f'양옆 공백 제거: ({k.strip()})')
print(f'왼쪽만 공백 제거: ({k.lstrip()})')
print(f'오른쪽만 공백 제거: ({k.rstrip()})')

s = '**밤*하늘의별***'
print(f'별표 제거: {s.strip('*')}') # 가운데 *은 제거 X
print('='*45)

# 문자열 바꾸기
w = 'It is spring'
next_w = w.replace('spring', 'summer')
print('문자열 바꾸기:', next_w)

s2 = s.replace('*', '') # 문자열에서 특정 문자 제거
print('별표 제거:', s2)
print('='*45)


# 문자열 나누기
k = 'Summer is coming'
print('문자열 나누기:', k.split())    # default 기준은 \s
a = k.split()
print(a[0], type(a), len(a))

date = '2024-04-07'
print('날짜를 기호 기준으로 나누기:', date.split('-'))
print('연도:', date.split('-')[0])

phone = '010-1234-5678'
print('핸드폰 번호 뒷자리:', phone.split('-')[-1])  # -1(뒤에서 첫번째) or 2(앞에서 3번째)












