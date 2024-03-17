'''
Q) 투자원금(money)과 투자기간(year)으로 원리금을 계산
이율은 6%(0.06) 으로 가정
원리금 공식 = 투자원금 x (1.0+이율)^투자기간

- 실행화면 -
5년 후의 원리금은 160.58706931200004
'''
money = 120 # 투자원금
year = 5 # 투자기간
amt = money * ((1.0 + 0.06) ** year)

# print(year, '년 후의 원리금은 ', amt, sep='')
print(f'''
투자원금 = {money}원
투자기간 = {year}년
{year}년 후의 원리금은 {amt}
''')





