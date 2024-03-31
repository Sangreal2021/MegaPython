'''
# 튜플(tuple)
튜플이름 = (데이터0, 데이터1, 데이터2, ..)
튜플 특징 : 순서 O, 중복 O, 변경 X

'''

a = (5, 10, 15, 10, 5)
b = (5, 10, 'Sun', 'day', 'Morning')
c = (0, True, ('Sun', 'day', 'Morning'))

print('a =', a, type(a))

# 튜플 인덱싱
print(a[1], a[-2])
print(a[2], a[-3])

print(b[2] + b[3])

print(c[0] + c[1]) # True = 1
print(c[-1][-1])
print('-'*40)

# 튜플 슬라이싱
print(a[2:])
print(b[0:5:2]) # [시작값:끝값:증감값]
print(b[::2])   # 전부 선택 후 2씩 건너뛰기
print(c[2][::2])
print('-'*40)
##################################################

d = (1, 2, 3, 4, 5)
e = (6, 7, 8)

f = d + e
print('f =', f)
g = e * 3
print('g =', g)

# 튜플 데이터를 index로 찾기
print(g.index(7))   # 가장 먼저 나오는 7의 인덱스 반환
print(g.index(7, 2))    # 2번째로 나오는 7의 인덱스 반환





