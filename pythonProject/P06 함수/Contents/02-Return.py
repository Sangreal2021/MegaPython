'''
# return문
    def 함수명(매개변수, ..):
        ...
        return 리턴값

함수를 선언할 때 return문의 작성 유무에 반환값의 존재 여부를 선택 가능함.

'''

# 함수 선언
def get_add(x, y):
    return x+y

# 함수 호출
result01 = get_add(10,20)
print(result01)

# 두 실수의 합을 반환
num = get_add(1.5, 3.7)
print(num, type(num))

# 두 문자열을 이어붙여서 반환
msg = get_add('묻고 ', '더블로가')
print(msg, type(msg))
####################################################

def get_avg(a, b, c):
    sum = a+b+c
    return sum/3

print('평균은', get_avg(15, 15,30))
print('평균은', get_avg(45, 25,20))
####################################################

def good_day():
    return '우마 입니다!'

print(good_day())




























