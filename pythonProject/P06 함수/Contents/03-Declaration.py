'''
함수 선언하기(function declaration)
# 함수 입출력 흐름
(입력) -> 함수 -> (결과)
(매개변수) -> 함수 -> (리턴값)

# 함수 구성 경우의 수
리턴값  매개변수   함수선언
---------------------------------------
X       X          f(): ...
O       X          f(): ... return 0
X       O          f(a): ...
O       O          f(a): ... return 0
---------------------------------------
# 함수 만들기
1. 만들려는 함수의 기능을 결정함.
2. 기능에 맞는 함수 이름을 정함.
3. 리턴값(출력)과 매개변수(입력)를 고려하여 함수를 만듬.
4. 함수이름과 매개값을 일치시켜 함수를 호출함.

'''

# 리턴X, 매개변수X 함수
# 예제1) "안녕하세요" 문자열을 5번 출력하는 함수를 만드시오.
def hello():
    for i in range(5):
        print('안녕하세요')
hello()
print('-'*50)

# 리턴O, 매개변수X 함수
# 예제2) "감사합니다" 문자열을 반환하는 함수를 만들고 출력문으로 확인하시오.
def thank():
    msg = "감사합니다"
    return msg


print(thank())
print('-'*50)

# 리턴X, 매개변수O 함수
# 예제3) 매개변수로 문자열과 숫자를 입력받고,
#    받은 숫자의 횟수만큼 받은 문자열 내용을 출력하는 함수를 작성.
def repeat_msg(num, msg):
    for i in range(num):
        print(msg)
repeat_msg(3, '우마입니다')
repeat_msg(msg='spring', num=2)
print('-'*50)

# 리턴O, 매개변수O 함수
# 예제4) 매개변수로 네 수를 입력받고 평균값을 리턴하는 함수를 작성하시오.
# num = int(input())
# def avg(num):
#     total = 0
#     for i in range(4):
#         total += num
# print('평균:', total/4)

def get_avg(a, b, c, d):
    return (a+b+c+d)/4

print(get_avg(1,2,3,4))

# 매개변수로 리스트를 입력받아서 평균값 리턴하는 함수
def average(a):
    return sum(a)/len(a)

k = [10, 20, 30]
print(average(k))
print(average([10,20,30,40]))
















