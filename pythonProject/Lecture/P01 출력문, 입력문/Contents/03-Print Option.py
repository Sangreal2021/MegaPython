#== 출력문 옵션 알아보기 ==#
# seperator : (,)사이에 출력할 데이터들을 sep='내용' 으로 연결
# (,)는 무조건 한 칸씩 띄워쓰기
print(2, 0, 2, 4) # sep=' ' 가 default
print(2, 0, 2, 4, sep=' ')
print(2, 0, 2, 4, sep='|')
print(2, 0, 2, 4, sep='')

print('2024', '03', '16', sep='-')
print('시험 난이도: TOEFL', ' TOEIC', sep=' >>>')
print('123 + 456', 123+456, sep=' = ')
print()


# end : 문자열의 마지막을 end='내용'으로 출력
# default 값 : end='\n'
print('원주율 : ', 3.141, sep='', end='')
print(592)
print()

print('3월 4월 5월', end='')
print()
print('6월 7월 8월')
print()

# sep, end 옵션 함께 사용하기
print(15, 27, sep=' + ', end=' = ')
print(15 + 27)
print()














