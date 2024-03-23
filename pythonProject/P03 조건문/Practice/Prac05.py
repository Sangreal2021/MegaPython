'''
Q) 물건의 금액을 입력받아
    할인율에 따른 할인금액을 구하시오.
    5000원 이상은 5%
    10000원 이상은 10%
    50000원 이상은 20%

    - 실행화면 -
    입력: 8000
    할인받는금액: 400
    - 실행화면 -
    입력: 20000
    할인받는금액: 2000
    - 실행화면 -
    입력: 60000
    할인받는금액: 12000
    - 실행화면 -
    입력: 3000
    할인받는금액: 0

'''

amt = int(input('입력: '))
rate = 0

# if 10000 > amt >= 5000:
#     rate = 0.05
# elif 50000 > amt >= 10000:
#     rate = 0.1
# elif amt >= 50000:
#     rate = 0.2
# else:
#     rate = 0

if amt >= 50000:
    rate = 0.2
elif amt >= 10000:
    rate = 0.1
elif amt >= 5000:
    rate = 0.05
else:
    rate = 0

discount = int(amt * rate)
print('할인받는금액:', discount)













