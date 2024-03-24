'''
Q)  구구단 3단을 출력하라.

    ↓ 실행화면 ↓
    3 x 1 = 3
    3 x 2 = 6
    3 x 3 = 9
    3 x 4 = 12
    3 x 5 = 15
    3 x 6 = 18
    3 x 7 = 21
    3 x 8 = 24
    3 x 9 = 27
'''
# 구구단 3단 출력
for i in range(1, 10):
    print(f'{3} x {i} = {3 * i}')
    # print('3 x', i, '=', 3*i)
print()
print('#' * 15)

# 구구단 전체 출력
for i in range(2, 10):
    print(f'<{i} 단>')
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
    print('')

















