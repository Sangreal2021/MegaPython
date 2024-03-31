# 1. 다음 주어진 리스트에서 "Tomato" 항목을 추가하고
#   "Apple" 항목을 삭제해서 리스트를 출력하시오.
a = ["Banana", "Apple", "Orange"]

a.append("Tomato")
a.remove("Apple")   # del a[1]
print(a)

# 2. 다음 주어진 튜플에 10부터 40까지의 값을 출력하고
#   튜플의 길이도 출력해보시오.
b = (-10, 0, 10, 20, 30, 40, 50)
print(b[2:6])   # 6 - 2 는 4개의 데이터 출력
print('b 튜플의 길이 =', len(b))