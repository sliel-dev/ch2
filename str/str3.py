# 문자열 안에서 문자 하나를 추출하기 위해 index를 사용
# H e l l o
# 0 1 2 3 4
print('Hello'[0])
print('Hello'[1])

# 문자 슬라이싱
# [index시작 : index끝] => 범위로 추출
print('hello'[0:2])
print('hello'[2:5])

# 끝과 시작을 비우기
# 2에서 시작해서 끝까지
print('hello'[2:])
# 처음부터 2까지
print('hello'[:2])

# 문자열의 길이를 구하는 함수 : len()
print(len('aaa'))
print(len('hello, world!'))
print(len('안녕하세요'))