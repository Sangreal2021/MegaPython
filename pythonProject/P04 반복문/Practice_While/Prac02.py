'''
Q)  사용자로부터 정수를 입력 받아서 계속 더하는 프로그램을 작성하자.
    사용자가 0을 입력하면 지금까지 입력된 모든 정수의 합계를 출력한다.
    Tip) 복합대입연산자 사용

    ↓ 실행화면 ↓
   정수 입력: 10
   정수 입력: 20
   정수 입력: 30
   정수 입력: 0
   합계: 60

'''

sum = 0
while True:
    num = int(input('정수 입력: '))
    sum += num
    if num == 0:
        break
print(f'합계: {sum}')

















