'''
# 관계연산자(비교연산자)
>, >=, <, <=, ==, !=
두 값을 비교한 결과를 참 또는 거짓으로 반환.

== : 서로 같은가?
!= : 서로 다른가?

a == b : a와 b가 같으면 True, 다르면 False
a != b : a와 b가 다르면 True, 같으면 False
'''

a = (10 > 5)  # True
b = (11 <= 10)
print('a =', a, type(a))
print('b =', b, type(b))
###########################################
num1 = 10; num2 = 20; num3 = 30

# '==' 연산자 는 서로 값이 같은지 확인
c = (num1 == num3)  # False
d = ((num1+num2)==num3) # True
print('c =', c)
print('d =', d)

# '!=' 연산자는 서로 값이 다른지 확인
e = (num1 != num3)
f = ((num1+num2)!=num3)
print('f =', f)


# 관계연산자는 동시에 여러 개 사용 가능 (C, Java 에서는 불가능)
print(num3 > num2 > num1)
print(num2 > num1 > num3) # (num2 > num1) && (num1 > num3)































