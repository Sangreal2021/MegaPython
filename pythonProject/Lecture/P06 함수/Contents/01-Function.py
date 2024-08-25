'''
# 함수(function)
함수는 어떤 기능들을 수행하는 실행문들의 모음.
한번 작성된 함수는 여러번 재사용 가능.
함수 작성시 입력 매개변수나 리턴값 반환 여부를 선택 가능함.

1. 함수 선언
    def 함수명(매개변수, ..):
        실행문..

함수를 선언하여 '함수명'이 어떤 기능들을 수행하도록 정함(define)

2. 함수 호출
    함수명(매개값, ..)

# 매개변수(parameter)
함수를 실행할 때 필요한 데이터를 외부로부터 입력받기 위한 변수
0개 또는 여러 개 작성 가능

'''
# 함수 선언
def hello():    # 매개변수 0개
    print('안녕하세요')

# 함수 호출
hello()
hello()
##################################################

# 함수 선언
def today(a):
    print('Today is', a)

# 함수 호출 - 매개값 1개 필요
today('Saturday')
today('sunny')
today(1)
today(True)
today(False)
##################################################

# 함수 선언
def add(x, y):  # 매개변수 2개
    print('두 수의 합:', x + y)

# 함수 호출
add(3,4)    # 매개값 2개 필요
a = 10
b = 20
add(a, b)
add(a, 100)
add('Java', 'Script')
# add(10, 'Script') # Error. 매개값 타입 일치시켜야 함
##################################################

# 함수 선언
def is_discount(price):
    if price >= 30000:
        print('배송비 무료입니다.')
    else:
        print('배송비 2500원 입니다.')

# 함수 실행
is_discount(50000)
is_discount(1000)
is_discount(10000)  # 함수 여러번 재사용 가능
##################################################

def repeat_msg(times):
    for i in range(times):
        print('2024-04-06')

repeat_msg(5)























