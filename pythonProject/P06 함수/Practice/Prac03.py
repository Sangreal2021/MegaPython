''' CodeUp 1577
    이 문제는 절댓값 함수를 구현하는 문제입니다.
    정수 하나를 입력 받고 함수를 실행시켜
    절댓값을 반환 받아 출력하는 코드를 작성하시오.
    함수명: myabs
    매개변수: 정수형 1개
    리턴값: 정수형 1개
    함수 내용 : 매개값에 대한 절댓값을 반환하는 함수 구현

    ↓ 입력 예시 ↓
    -1

    ↓ 출력 예시 ↓
    1
'''
def myabs(n):
    abs_num = abs(n)
    return abs_num

num = int(input())
print(myabs(num))

# def myabs(n):
#     if n < 0:
#         return -n
#     else:
#         return n
#
# # 정수 입력 및 함수 실행
# n = int(input())
# print(myabs(n))

