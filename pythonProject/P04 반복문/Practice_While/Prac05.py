'''
Q)  항공사에서 짐을 부칠 때 10kg이상이면 수수료 10,000원을 내야합니다.
    만약 10kg미만이라면 수수료는 따로 없습니다.
    짐의 무게를 입력 받아서 지불할 금액을 계산하는 프로그램을 작성하시오.
    (무게에 0을 입력하는 경우는 프로그램을 종료합니다.)

    ↓ 실행화면 ↓
    짐의 무게는 얼마입니까? 8
    수수료는 없습니다.

    짐의 무게는 얼마입니까? 15
    수수료는 10,000원입니다.

    짐의 무게는 얼마입니까? 0
    프로그램 종료
'''

# while True:
#     num = int(input('짐의 무게는 얼마입니까? '))
#     if num == 0:
#         print('프로그램 종료')
#         break
#     if num >= 10:
#         print(f'짐의 무게 {num}kg에 대한 수수료는 10,000원입니다.', end='\n\n')
#     else:
#         print(f'짐의 무게 {num}kg에 대한 수수료는 없습니다.', end='\n\n')

while True:
    num = int(input('짐의 무게는 얼마입니까? '))
    if num == 0:
        print('프로그램 종료')
        break
    elif num >= 10:
        print(f'짐의 무게 {num}kg에 대한 수수료는 10,000원입니다.')
    else:
        print(f'짐의 무게 {num}kg에 대한 수수료는 없습니다.')
    print()

# # 정삼각형  별찍기
# n = int(input('삼각형의 높이를 입력하세요 >>> '))
# for i in range(1, n+1):
#     print(' ' * (n-i), end='')
#     print('*' * (2*i - 1))







