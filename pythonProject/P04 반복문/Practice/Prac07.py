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
    - 정삼각형

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


# Q2)
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
