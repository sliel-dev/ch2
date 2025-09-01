# 문자열 관련 함수
# replace() : 문자열 교체 함수
print('banana'.replace('ba', 'na'))

# 전화번호에서 -을 :으로 교체
# replace(교체대상, 교체내용)
print('010-1234-5678'.replace('-', ':'))

# 전화번호에서 -을 제거
print('010-1234-5678'.replace('-', ''))

# repr 따옴표를 표시하는 함수
print('hello')
print(repr('hello'))

# 공백 제거 함수
print(repr(' hello world '.strip()))
print(repr(' hello world '.lstrip()))
print(repr(' hello world '.rstrip()))

# title() 첫글자만 대문자로 바꾸는 함수
print('hello world'.title())