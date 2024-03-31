#1. 다음 주어진 리스트에서 "Tomato" 항목을 추가하고
#   "Apple" 항목을 삭제해서 리스트를 출력하시오.
a = ["Banana", "Apple", "Orange"]

a.append("Tomato")
a.remove("Apple")   # del a[1]
print(a)