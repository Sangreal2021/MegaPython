'''
Q) 사용자로부터 입력 받은 두 수의 합과 차를 구하여 출력하시오.
    단, 두 수의 차는 값이 양수가 나오도록 출력하시오.

- 실행화면 -
정수 입력: 30
정수 입력: 50
두 수의 합은 80
두 수의 차는 20

'''

score1 = int(input('정수 입력: '))
score2 = int(input('정수 입력: '))
plus = score1 + score2
minus = abs(score1 - score2)

# 방법1
# print(f'''두 수의 합은 {plus}
# 두 수의 차는 {minus}
# ''')

# 방법2
# print('두 수의 합은', plus)
# # if-else문
# if score1 > score2:
#     print('두 수의 차는', score1-score2)
# else:
#     print('두 수의 차는', score2-score1)

# 방법3
# if문 한번 사용
sub = score1 - score2
print('두 수의 합은', plus)
if sub < 0:
    # sub = score2 - score1
    sub = -sub
print('두 수의 차는', sub)




















