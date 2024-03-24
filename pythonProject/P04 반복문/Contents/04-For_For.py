'''
중첩 반복문
    for i in range(a, b):       # 외부 for문
        반복문A
        for j in range(c, d):   # 내부 for문
            반복문B
        반복문C

실행 순서
    외부 for문에 진입하면
        반복문A 를 먼저 수행하고,
        내부 for문에 진입해서 반복문B를 반복 수행하고,
        반복문C를 수행한 후
    다시 외부 for문 처음으로 돌아가서 반복을 진행
'''

# 이중 for문
for i in range(1, 6):
    for j in range(1, 4):
        print(f'i = {i} | j = {j}')
print('#' * 20)
print()

# 구구단 3단
for j in range(1, 10):
    print(f'{3} x {j} = {3 * j}')
print('#' * 20)
print()

# 구구단 출력하기1
# for i in range(2, 10):
#     print(f'<구구단 {i}단>')
#     for j in range(1, 10):
#         print(f'{i} x {j} = {i * j}')
#     print('=' * 20)

'''
예제) 구구단 출력하기2 
2단: 2 4 6 8 10 12 14 16 18
3단: 3 6 9 12 15 18 21 24 27
4단: 4 8 12 16 20 24 28 32 36
5단: 5 10 15 20 25 30 35 40 45
6단: 6 12 18 24 30 36 42 48 54
7단: 7 14 21 28 35 42 49 56 63
8단: 8 16 24 32 40 48 56 64 72
9단: 9 18 27 36 45 54 63 72 81
'''

for i in range(2, 10):
    print(f'<구구단 {i}단> :', end=' ')
    for j in range(1, 10):
        print(f'{i * j}', end=' ')
    print('')
