'''
# 딕셔너리(Dictionary)
딕셔너리이름 = {key:value, key:value, ..}
딕셔너리 특징 : 순서 X, key 중복 X, 변경 O
'''

a = {'name': '너구리', 'birth': '5/1', 'age': 10}
b = {0: 'today', 2: 'is', 1: 'sunday'}
c = {1: 20, 2: 40, 3: 60}
d = {'num1': 100, 'num2': 200}
e = {'pet': ['dog', 'cat'], 'wild': ('tiger', 'lion', 'bear')}

print('딕셔너리a 길이:', len(a))
print('딕셔너리e 길이:', len(e))
print('딕셔너리e의 wild 길이:', len(e['wild']))

# key 값으로 value 값 접근
print(a['name'])
print(b[2])  # key 값이 2
print(c[3])  # key 값이 3
print(d['num1'])
print(e['pet'])
print(e['pet'][0])
print('-' * 40)

# 딕셔너리 데이터 추가, 수정, 삭제
# 1. 추가
a['hobby'] = 'Youtube'  # 딕셔너리명[새로운key] = value
print(a)
c[4] = 80
print(c)

# 2. 수정
a['name'] = 'nuguri'  # 기존 key에 value 대입하여 수정
print(a)

# 3. 삭제
del a['hobby']  # 해당 key와 value가 함께 삭제
print(a)
del c[4]
print(c)
