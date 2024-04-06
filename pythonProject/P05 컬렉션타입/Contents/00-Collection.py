'''
# == 컬렉션타입 == #
여러 개의 데이터를 저장하고 관리하는 자료형
리스트(★★★), 튜플, 딕셔너리(★★), 집합

# == 컬렉션타입과 반복문 == #
    for 변수 in 컬렉션타입:
        반복문..

'''

listA = [10, 20, 30, 20, 10]
tupB = (10, 20, 30, 20, 10)
dictC = {'a': 10, 'b': 20, 'c': 30}
setD = {10, 20, 30, 20, 10}

print('listA =', listA)
print('tupB =', tupB)
print('dictC =', dictC)
print('setD =', setD)  # 집합은 중복값 제거
print('='*45)

# == 컬렉션타입과 반복문 == #
for data in listA:
    print(data, end=' ')
print()

for data in (10, 20, 30, 20, 10):   # tupB
    print(data, end=' ')
print()

for key in dictC:  # 딕셔너리는 기본값으로 key를 가져옴
    print(key)
print()

for key in dictC:
    print(key, dictC[key]) # key, value 출력
print()













