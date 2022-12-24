'''
내장함수 보충
'''

# formatting
result = format(10000) # str(10000)과 같다, "10000"
print(type(result))
result = format(10000, ',') # 1000 단위로 끊어준다
print(result)

# 절대값
result = abs(10)
print(result)
result = abs(-10)
print(result)

# max() 최대값 반환
# min() 최소값 반환
result = max(1, 9)
print(result)
li = [3, 4, 5, 2, 1]
print(max(li))

# pow() 거듭제곱 함수
result = pow(10, 2)
print(result)

# sorted() 함수 - 오름차순 정렬
my_li = [5, 6, 3, 4, 1, 2]
result = sorted(my_li)
print(result) # [1, 2, 3, 4, 5, 6]

result = sorted(my_li, reverse = True)
print(result) # 내림차순 정렬

# zip()함수 - 같은 인덱스 끼리 튜플로 묶어준다(연결한다,join)
names = ['james', 'emily', 'amanda']
scores = [60, 70, 80]

for student in zip(names, scores):
    print(student) # tuple

print(type(zip(names, scores))) # class zip // tuple array?

for name, score in zip(names, scores):
    print('{}의 점수는 {}점 입니다.'.format(name, score))

print(zip(names, scores)) # 메모리 주소 반환
print(id(zip(names, scores))) # 고유 번호 반환