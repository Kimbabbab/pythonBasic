# join() 메소드
s = '-'.join('python')
print(s)

print('python'.join('-'))
print('python'.join('--'))

# alt + ctrl + l ; 자동 정렬
s = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)
print(type(s)) # class 'str'

print(''.join(['a', 'b', 'c', 'd', 'e']))

# split() 메소드
s = 'Life is  too short'
result = s.split() # list, 공백으로 나눠준다
print(result)
print(s.split(' '))

s = '010-1234-5678'
result = s.split('-')
print(result)

name = '전정현|23|대학생'
result = name.split('|')
print(result)
print('이름 : {}'.format(result[0]))

# replace()
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() 공백제거
s = '   apple   '
print(s)
print(s.strip()) # 양쪽 공백 제거
print(s.lstrip()) # 왼쪽 공백 제거
print(s.rstrip()) # 오른쪽 공백 제거

# 전체 공백 제거
s = ' a p p l e '
print(s)
print(s.strip()) # 내부의 공백은 제거해 주지 못한다

result = s.replace(' ', '')
print(result)
print(type('')) # 문자가 없는 String