'''
Q) 3개의 정수를 입력받은 후,
평균값을 계산하여 정수로 결과를 나타내보자

- 실행화면 -
정수를 입력하시오: 10
정수를 입력하시오: 20
정수를 입력하시오: 30
평균은 20
'''
num1 = int(input('정수를 입력하시오: '))
num2 = int(input('정수를 입력하시오: '))
num3 = int(input('정수를 입력하시오: '))
avg = int( (num1+num2+num3) / 3 )
# print(f'''평균은 {avg}입니다.
# ''')
print('평균은 ', avg, '입니다.', sep='')
