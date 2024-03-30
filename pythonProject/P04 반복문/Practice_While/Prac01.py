'''
Q)  while문을 사용하여 하나의 자연수를 입력하면
    다음처럼 카운트 다운을 하도록 출력하시오.

    ↓ 실행화면 ↓
    자연수를 입력하세요: 5
    5
    4
    3
    2
    1
'''

num = int(input('자연수를 입력하세요: '))

# 방법 1
# while num != 0: # num >= 1:
#     print(num)
#     num -= 1

# 방법 2
while True:
    print(num)
    num -= 1
    if num == 0:
        break














