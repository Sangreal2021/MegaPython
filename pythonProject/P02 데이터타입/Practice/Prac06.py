'''
Q) 2개의 실수를 입력 받아서 두 수의 정수 부분만 더한 값을 출력해보자.
    int() 캐스팅은 소수점 절삭 특징이 있음!!

- 실행화면 -
첫 번째 실수를 입력하시오: 1.67
두 번째 실수를 입력하시오: 2.45
정수 부분의 합은 3
'''

input1 = float(input('첫 번째 실수를 입력하시오: '))
input2 = float(input('두 번째 실수를 입력하시오: '))
sum = int(input1) + int(input2)

print(f'''
첫 번째 입력값 = {input1}
두 번째 입력값 = {input2}
정수 부분의 합은 {sum}
''')
# print('정수 부분의 합은', sum)







