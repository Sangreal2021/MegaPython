'''
# elif(else if)문
조건식이 여러 개인 경우 사용
elif문은 여러 개 사용 가능

# if - elif - else

    if 조건식A:
        (조건식A가 참이면 실행)
        실행문..
    elif 조건식B:
        (조건식A가 거짓이고 B가 참이면 실행)
        실행문..
    elif 조건식C:
        (조건식A, B가 거짓이고 C가 참이면 실행)
        실행문..
    ...
    else:
        (위에 모든 조건식들이 거짓이면 실행)
        실행문..

'''

# array = ['art', 'music', 'sports']
# subject = input('과목 입력 >>> ')
# if subject == 'art':
#     print('그림을 그립니다.')
# elif subject == 'music':
#     print('노래를 부릅니다.')
# elif subject == 'sports':
#     print('공을 찹니다.')
# else:
#     print('개설된 과목이 아닙니다.')

# Q) 점수에 따른 성적 등급 나타내보기
# 90점 이상 : A
# 80점 이상 90점 미만 : B
# 70점 이상 80점 미만 : C
# 60점 이상 70점 미만 : D
# 60점 미만 : F
score = int(input('점수 입력 >>> '))
if score >= 90:
    print('점수:', score, '성적:', 'A')
elif score >= 80:
    print('점수:', score, '성적:', 'B')
elif score >= 70:
    print('점수:', score, '성적:', 'C')
elif score >= 60:
    print('점수:', score, '성적:', 'D')
else:
    print('점수:', score, '성적:', 'F')

























