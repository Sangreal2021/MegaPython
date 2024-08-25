'''
Q) 주어진 정수의 약수를 모두 찾아내는 함수를 작성하시오.
    사용자로부터 정수를 입력받아
    해당 정수의 약수를 모두 출력하느 ㄴ함수를 만들고 실행하시오.
    함수명 : show_divisor
    매개변수 : 정수형 1개
    리턴값 : 없음

    - 실행화면 -
    정수 입력: 8
    1 2 4 8
'''

# 선언된 함수는 메모리에 올라감
def show_divisor(n):            # 함수 선언
    for i in range(1, num + 1):
        if (num % i) == 0:
            print(i, end=' ')

num = int(input('정수 입력: ')) # 입력문
show_divisor(num)               # 함수 실행

