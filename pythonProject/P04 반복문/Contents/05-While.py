'''
# while 반복문
while문은 무한반복 혹은 반복할 횟수가 정해지지 않았을 때 사용함.

    while(조건식):
        반복문..

조건식이 참이면 반복 게속 진행
조건식이 거짓이 되면 반복 중지

'''

# 1~3까지 반복하기
i = 1
while i<=3:
    print(i)
    i += 1 # 증감식 필수
print('-' * 15)

# == for문과 while문의 비교 == #
# 0~4까지 5번 반복
for i in range(1, 5): # (시작값, 끝값, 증감식)
    print(i)
print('-' * 10)

# while문 ~
w = 0 # 시작값
while (w < 5): # 끝값
    print(w)
    w += 1 # 증감식
print('-' * 10)

# 1~10까지 합 구하기
# sum = 0
# i = 1
sum, i = 0, 1
while (i <= 10):
    sum += i
    i += 1
print('sum :', sum)
print('-' * 10)

# 1~20까지의 홀수 한줄로 출력하기
i = 1
# while i != 20:
while i <= 20:
    if i%2 == 1:
        print(i, end=' ')
    i += 1






















