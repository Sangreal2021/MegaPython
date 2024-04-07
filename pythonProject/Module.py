'''
# 모듈(module) - 파이썬 코드 파일
    import 모듈이름

모듈은 변수나 함수 또는 클래스 등의 파이썬 코드를 작성해 놓은 파일.
모든 코드들을 직접 만들어서 사용할 수 없기에,
많이 사용되거나 유용한 기능들을 미리 작성해둔 모듈을 가져와서 사용함.

표준 모듈: 파이썬에 기본으로 내장되어 있는 모듈
    math, random, datetime, time, system, ...

외부 모듈: 다른 사람들이 만들어서 배포한 모듈. 추가적으로 다운로드 필요
    numpy, pandas, beautifulsoup, ..

'''
# 1. math 모듈
import math

print(math.pi)  # pi
print(math.e)   # 지수값
PI = math.pi
print(math.sin(PI/2))
print(math.cos(PI/2))
print(math.floor(PI))   # 내림
print(math.ceil(PI))   # 올림
print(round(3.14))   # 반올림. 기본제공함수
print('-'*45)

# cf) 기본제공 함수
nums = [1,2,3,4,5]
print(sum(nums))
print(len(nums))
print(max(nums))
print(abs(-11.5))
print('-'*45)

# from 모듈명 import * : 바로 참조없이 모듈 사용가능
from math import *
print(sin(PI/2))
print('-'*45)


# 2. random 모듈 (as로 별칭 가능)
import random as rd

print(rd.random())  # 0 ~ 1 사이
print(rd.uniform(10, 15))   # 해당 범위 랜덤한 실수 리턴(10이상, 15미만)
print(rd.randrange(1, 5, 2))   # 랜덤 정수 리턴(1이상, 5미만, 증감값)
print(rd.randint(1, 45)) # 랜덤 정수 리턴(1이상, 45이하)
print(rd.sample([1,2,3,4,5], 2)) # 모집단, 표본개수
print('-'*45)


# 로또 번호 생성하기
a = [i for i in range(1, 46)]   # i에 1~45까지를 반복해서 넣음
# print(a)
lotto = rd.sample(a, 6)
lotto.sort()
print('로또 번호:', lotto)
print('-'*45)


# 3. datetime 모듈
import datetime as dt
print(dt.datetime.now())
now = dt.datetime.now()
print(f'{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초')
print('-'*45)


# 4. time 모듈 (시간 기능)
import time as t

print('3초간 정지..')
t.sleep(3)
print('후 실행합니다.')













