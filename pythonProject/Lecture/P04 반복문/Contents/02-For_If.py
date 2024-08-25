'''
for i in range(a, b):
    if 조건식:
        실행문..


'''

# 짝수 출력하기
for i in range(1, 20):
    if i%2 == 0:
        print(i, end=' ')
print()

# 7의 배수 출력하기
for i in range(1, 100):
    if i%7 == 0:
        print(i, end=' ')
print()

# 월드컵 개최년도 출력하기
for i in range(2002, 2023):
    if i%4 == 2: # (i-2002)%4 == 0:
        print(i, end=' ')
print()





