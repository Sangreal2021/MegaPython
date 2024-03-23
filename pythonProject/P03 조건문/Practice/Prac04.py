'''
Q) 사용자가 신호등의 색깔을 입력하면 R, G, Y 각각에 대하여
    '정지!', '진행~', '주의'와 같은 멘트를 출력하는 프로그램을 만드시오.
    단, 대소문자 모두 인식하도록 작성하시오.

    - 실행화면 -
    신호등의 색깔 입력(R, G, Y): r
    정지!

    - 실행화면2 -
    신호등의 색깔 입력(R, G, Y): G
    진행~
'''
# sign = input('신호등의 색깔 입력(R, G, Y): ')
# if sign == 'r' or sign == 'R':
#     print('정지!')
# elif sign == 'g' or sign == 'G':
#     print('진행~')
# elif sign == 'y' or sign == 'Y':
#     print('주의')

import re
sign1 = input('신호등의 색깔 입력(R, G, Y): ')
if re.match(sign1 == 'r', re.IGNORECASE):
    print('정지!')
elif re.match(sign1 == 'g', re.IGNORECASE):
    print('진행~')
elif re.match(sign1 == 'y', re.IGNORECASE):
    print('주의')













