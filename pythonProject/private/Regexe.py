import re
'''
한자 정규표현식
'''
# 정규표현식 패턴 정의
# pattern = r"[\u4E00-\u9FFF\u3400-\u4DBF\U00020000-\U0002A6DF]+"
pattern = r"[ぁ-ゔァ-ヴー々〆〤一-龥]"

# 테스트 문자열
text = "这是一些汉字文本。 안녕 1521 !@#$$%%^ hello~"

# 정규표현식 검색
matches = re.findall(pattern, text)

# 한자들을 한 줄의 문자열로 연결하여 출력
print("Found Chinese characters:", ''.join(matches))
# print("Found Chinese characters:", matches)
