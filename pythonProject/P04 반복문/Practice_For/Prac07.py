'''
Q1) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성하시오.

↓ 실행화면 ↓
*
**
***
****
*****

Q2) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성하시오.
    *
   **
  ***
 ****
*****

도전과제) 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성하시오.
        (Tip: 각 줄의 *개수는 2n-1)

↓ 실행화면 ↓
    *
   ***
  *****
 *******
*********

i번째줄:    1   2   3   4   5   n번째줄
blank:   4   3   2   1   0   (5-n)개
star :   1   3   5   7   9   (2n-1)개
length  5   6   7   8   9   n+4

'''

for i in range(1, 6):
    for j in range(1, 6):
        print('*', end='')
    print('')
print('')

for i in range(5, 0, -1):
    print('*' * i)
print('')

for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print('')
print('')

for i in range(5, 0, -1):
    print('*' * i)
print('')

# n = int(input('정삼각형의 높이를 입력하세요 >>> '))
# for i in range(1, (n+1)):
#     print(' ' * (n-i), end='')
#     print('*' * (2*i - 1))

# 문자열 * 숫자
for i in range(1, 6):
    print("*" * i)
print()


# Q2) 위의 좌우반전
for i in range(1, 6):
    print((' ' * (5-i)) + ('*' * i))
print()

for i in range(1, 6):
    for j in range(5-i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print('')
print()
