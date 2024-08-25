'''
# 집합(Set)
집합이름 = {데이터, 데이터, 데이터, ...}
집합 특징 : 순서 X, 중복 X, 변경 O

'''

a = {10, 20, 30, 20, 10}
b = {'How', 'was', 'your', 'day'}
c = set('sakura')

print(a, type(a), len(a))   # 숫자는 출력할 때만 오름차순
print(b)    # 순서 일정 X
print(c)
print('-'*45)

# 집합 데이터 추가, 삭제
s = {1, 2, 3}
s.add(4)            # 하나씩 추가
print(s)
s.update([5, 6, 7]) # 여러 개 추가
print(s)
s.remove(2)
print(s)
print('-'*45)

# 교집합, 합집합, 차집합
s1 = {1,2,3,4}
s2 = {3,4,5,6}

print('교집합:', s1 & s2)
print('합집합:', s1 | s2)  # UNION
print('차집합:', s1 - s2)

# 비트연산자
print(1 & 1)
print(1 & 0)
print(1 | 0)

# 비어있는 집합 만들기
k = {}  # 딕셔너리로 인식
print(k, type(k))

k = set()   # 비어있는 집합 생성
print(k, type(k))
k.add(10)
print(k)















