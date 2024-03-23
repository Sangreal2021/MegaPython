'''
Q) 자연수를 입력 받아서 홀수인지 짝수인지 판별하여 출력하시오.

- 실행화면 -
자연수를 입력하세요: 30
짝수입니다.

'''

n = int(input('자연수를 입력하세요: '))
if (n % 2) == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')


# kor = int(input('국어 성적 >> '))
# eng = int(input('영어 성적 >> '))
# math = int(input('수학 성적 >> '))
# total = kor + eng + math
# avg = total / 3
# if avg >= 90:
#     print('총점:', total, '평균:', avg, '성적:', 'A')
# elif 90 > avg >= 80:
#     print('총점:', total, '평균:', avg, '성적:', 'B')
# elif 80 > avg >= 70:
#     print('총점:', total, '평균:', avg, '성적:', 'C')
# elif 70 > avg >= 60:
#     print('총점:', total, '평균:', avg, '성적:', 'D')
# else:
#     print('총점:', total, '평균:', avg, '성적:', 'F')