'''
# if - else 조건문
- 조건식의 결과에 따라서 실행내용을 선택하여 수행

    if 조건식:
        (if조건식이 참이면 실행)
        실행문1
        실행문2
        ...
    else:
        (if조건식이 거짓이면 실행)
        실행문3
        실행문4
        ...

'''

# n = float(input('숫자 입력 >>> '))
# if n >= 50:
#     print('50보다 크거나 같습니다.')
# else: # if n < 50:
#     print('50보다 작습니다.')


# 어떤 수가 3의 배수인지 아닌지 확인하기
# a = int(input('정수 입력 >>> '))
# if (a % 3) == 0: # 어떤 수를 3으로 나누었을 때 나머지가 0이면 3의 배수
#     print('3의 배수입니다.')
# else:
#     print('3의 배수가 아닙니다.')


# Q) 사용자로부터 점수를 입력받아서 70점 이상이면 "합격"
#    70점 미만이면 "불합격" 메세지가 출력되도록 코드를 구현하시오~
score = int(input('성적 입력 (정수) >>> '))
if score >= 70:
    print('합격!')
else:
    print('불합격..')




















