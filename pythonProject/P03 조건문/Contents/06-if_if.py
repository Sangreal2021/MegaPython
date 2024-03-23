'''
# 중첩 조건문
    - if문 안에 새로운 if문 을 추가
'''

# 중첩 조건문
age = int(input('나이 입력 >>> '))
height = int(input('키 입력 >>> '))
if age >= 14:
    if height >= 160:
        print('번지점프 가능')
    elif height >= 140:
        print('락스핀 가능')
    else:
        print('롤러코스터 탑승 가능')
else:
    print('회전목마 올라가자')























