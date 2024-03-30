'''
# while 무한루프 형태
조건식을 참으로 시작하여 반복문 무한 실행
반복을 멈추려면 조건문과 break 명령문이 필요

    while True:
        반복문
        if 조건식:
            break

# break 키워드
반복문을 빠져나옴. 탈출(exit)
조건문과 함께 사용
'''

# 1~5 반복
# if 문 위치에 따라 조건이 바뀜
k = 1
while True:
    print(k)
    if k > 4:   # k == 6:
        break
    k += 1
print('-'*25)

# 1~20 사이 짝수 출력하기
a = 1
while True:
    if a%2 == 0:
        print(a, end=' ')
    a += 1
    if a == 21:
        break
print()
print('-'*25)

# == 입력 받아서 while문 탈출하기 == #
# 'Q'를 입력하면 무한반복 종료되도록
# while True:
#     print('반복을 멈추려면 Q를 입력하세요')
#     a = input('입력: ')
#     if a == '!Q':
#         break
# print('-'*25)

# 숫자 -1을 입력하면 무한반복 종료
while True:
    # num = int(input('숫자 입력(종료는 -1) : '))
    num = input('숫자 입력(종료는 -1) : ')
    if num == '-1':
        print('프로그램을 종료합니다.')
        break














