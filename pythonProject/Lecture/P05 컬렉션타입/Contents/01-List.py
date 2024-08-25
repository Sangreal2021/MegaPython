'''
# 리스트(List)
리스트이름 = [데이터0, 데이터1, 데이터2, ..]
데이터에 순서를 매겨 늘어놓은 자료구조
리스트 특징 : 순서 O, 중복 O, 변경 O

'''
a = [10, 20, 30, 20, 10]
b = [5, 10, 'Sun', 'day', 'Morning']
c = [0, True, ['Sun', 'day', 'Morning']]

# 리스트 인덱싱
print('a =', a, type(a))
print(a[0])
print(a[1] + a[2])
print(a[-1])  # 끝에서 1번째 데이터
print('-' * 40)

print('\nb =', b)
print(b[2], b[-3])
print(b[2] + b[3], b[4])
print(f'{b[-1] * 4}')
print('-' * 40)

print('\nc = ', c)
print(c[2])
print(c[2][0])  # 이중리스트 데이터 접근
print(c[2][0] + c[2][1], c[2][2])
# print(f'{c[2][0] + c[2][1]} {c[2][2]}')
print('-' * 40)

# 리스트 슬라이싱
print(a[1:4])  #
print(a[:3])  # 처음부터 2번째 인덱스까지
print(a[:-1])  # 젤 마지막 인덱스 제외 모두 출력
print('-' * 40)

print(b[1:])  #

print(c[1:2])  # 1번 인덱스
print(c[2][:2])  # 내부리스트 2번 인덱스 전까지
print('-' * 40)

###################################################
d = [1, 2, 3, 4, 5]
e = [6, 7, 8]

# 리스트 연산 (문자열 연산과 동일)
print(d + e)
print(d * 2)

# 리스트 길이 구하기
print(len(d))
print(len(d + e))
print('-' * 40)

###################################################
f = [1, 2, 4]

# == 리스트 데이터 추가, 수정, 삭제 == #
# 1. 추가 (append)
f.append(100)  # 리스트 끝에 새로운 데이터 추가
print(f)
f.append('3월')
print(f)

f.insert(2, 3)  # 해당 인덱스에 데이터 추가
print(f)
f.insert(-1, '2월')
print(f)
print('-' * 40)

# 이중 리스트에 데이터 추가
k = [[1, 2, 3]]
k[0].append(4)
print(k)
k.append('밖')
print(k)
print('-' * 40)

# 2. 수정
f[4] = 5  # 리스트 인덱스 데이터 수정
print(f)
f[2:5] = [4, 8, 16]
print(f)
print('-' * 40)

# 3. 삭제
del f[5]  # 해당 인덱스의 데이터 삭제
print(f)
del f[-2]
print(f)
del f[1:4]
print(f)

f.remove(1)  # 해당 값을 삭제 (중복시 맨 앞에 하나 삭제)
print(f)
f.remove('3월')
print(f)
print('=' * 40)

# 비어있는 리스트 만들기
k = []
print(k, type(k))
k.append(10)
print(k)

k = list()
print(k, type(k))
k.append(20)
print(k)
print('=' * 40)
###################################################
# == 리스트 관련 함수 == #
nums = [10, 30, 20, 5, 25]
alp = ['a', 'c', 'f', 'b']

# 찾으려는 데이터 인덱스 반환
print(nums.index(20))
print(alp.index('c'))

# 오름차순 정렬
nums.sort()
print(nums)
alp.sort()  # ASC
print(alp)

# 내림차순 정렬
nums.sort(reverse=True) # DESC
print(nums)
alp.sort(reverse=True)
print(alp)

# 리스트 확장 (+ 연산과 append 기능 복합)
nums.extend([0, -5, -10])
print(nums)
nums.extend(alp)
print(nums)

# 역순으로 정렬 (오름/내림 차순이 아니고 그대로 뒤집기)
nums.reverse()
print(nums)

# 데이터 비우기
nums.clear()
print(nums)
print('=' * 40)

# 복합대입연산자 사용
a = [1, 2, 3]
a += [4, 5]  # 더할때 튜플()로 더해도 됨. 집합{} 도 가능
print(a)
a *= 2
print(a)

b = '아메'
b += '리카노'
print(b)
b = b.replace('메', '아')
print(b)
