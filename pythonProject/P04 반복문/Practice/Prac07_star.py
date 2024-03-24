'''
별찍기
'''
# 정방향
# height = int(input('삼각형의 높이를 입력하세요 >>> '))
# for i in range(1, height+1):
#     print("*" * i)

# 역방향
# height = int(input('삼각형의 높이를 입력하세요 >>> '))
# for i in range(height, 0, -1):
#     print('*' * i)

# 정삼각형
n = int(input('삼각형의 높이를 입력하세요 >>> '))
for i in range(1, n+1):
    print(' ' * (n-1), end='')
    print('*' * (2*i -1))