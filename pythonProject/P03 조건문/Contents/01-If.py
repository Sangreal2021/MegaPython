'''
# if 조건문
- 조건식의 결과가 참이면 내부 실행문들을 수행

    if 조건식:
        실행문1
        실행문2
        ...

'''
num = -10
if num > 0: # if 조건식:
    # 조건식이 참일 경우 실행할 공간
    # 조건식이 거짓이면 실행X
    print('조건문이 참입니다.')
    print('num은 양수입니다.')
print('조건문 끝나고 실행하는 문장')

num1 = float(input('숫자를 입력하세요 >>> '))
if num1 > 0:
    print('PLUS')
elif num1 == 0:
    print('Zer0')
else:
    print('MINUS')
























