'''
# for 반복문
    - for문은 코드 실행을 정해진 횟수만큼 반복할 때 사용함.

# for문의 일반적인 형태
    - for 반복변수 in 범위:
        반복문..

##############################################################
# for문과 range()
    for i in range(a, b):
        반복문..

1. a부터 (b-1)까지 반복
2. range(시작값, 끝값) - 초일산입, 말일불산입
3. i의 범위 : a <= i < b

##############################################################
# 다른 형태
for i in range(b):
    반복문..
1.b번 반복
2. range(끝값)
3. i 의 범위: 0 <= i < b

##############################################################
# 다른 형태
for i in range(a, b, n):
    반복문..
1. a부터 (b-1)까지 n만큼 건너 뛰며 반복
2. range(시작값, 끝값, 증감값)
3. a, b, n 은 정수만 사용 가능!
'''

# == for i in range(a, b): == #
# 1. 0~4까지 5번 반복
# for i in range(0,5):
#     print(i)

# 2. 1 ~ 10까지 숫자 출력
for i in range(1, 11):
    print(f"{i * 10}", end=' ')
print()
print('=' * 25)

# 3. 4~7까지 숫자 한줄로 출력
for i in range(4, 8):
    print(i, end=' ')
print()
print('=' * 25)


# 구구단 출력하기

# # 1단부터 9단까지 반복
# for i in range(1, 10):
#     # 각 단의 구구단 출력
#     print(f"<{i}단>")
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i*j}")
#     # 단과 단 사이에 구분을 위한 빈 줄 출력
#     print("")


# === for i in range(b): === #
# 0~4까지 5번 반복
for i in range(5):
    print(i)
print()

# '일요일' 4번 출력
for i in range(4):
    print('일요일', end=' ')
print()

# '=' 기호 10개 한줄로 출력
for i in range(10):
    print('=', end='')
print()

# == for i in range(a, b, n): == #
# 1~10 밤위에서 숫자 2씩 건너뛰면서 한줄로 출력
for i in range(1, 11, 2):
    print(i, end=' ')
print()

# 1~40 범위 사이 3의 배수만 한줄로 출력
for i in range(3, 40, 3):
    print(i, end=' ')
print()

# 10~1 범위에서 숫자 2씩 감소하면서 한줄로 출력
for i in range(10, 0, -2):
    print(i, end=' ')
print()

# '카운트다운' 5~1까지 출력
for i in range(5, 0, -1):
    print('카운트다운', i)





















