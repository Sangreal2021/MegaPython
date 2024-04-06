'''
Q)  반복문을 사용하여 다음 리스트 값들 중에서
    최대값과 최소값을 찾고 평균값을 구하시오.

    ↓ 실행화면 ↓
    최대값: 85
    최소값: 3
    평균값: 42.875
'''
k = [20, 55, 10, 3, 85, 36, 70, 64]

max = k[0]
min = k[0]
total = 0
for i in k:
    if i > max:
        max = i
    if i < min:
        min = i
    total += i
avg = total/len(k)

# print('최대값:', max)
# print('최소값:', min)
# print('평균값:', avg)

# 결과 항목들을 딕셔너리로 표현하기
result = {'최대값':max, '최소값':min, '평균값':avg}
for key in result:
    print(f'{key}: {result[key]}')












