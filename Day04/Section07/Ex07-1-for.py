'''
for문
    값의 범위나 횟수가 정해져 있을 때
    사용하면 편리한 반복문
    while문 보다 자주 사용된다.
    
for 변수 in 반복가능한객체: // 인덱싱이 가능한 객체 e.g) list, tuple, String 등
    반복실행문

'''

pwd = input('문자와 숫자가 모두 포함된 비밀번호를 입력하세요 >>> ') # String
ch_count = 0
num_count = 0

# pwd =  1ac35
# index) 01234

for ch in pwd:
    if ch.isalpha(): # String 내장 메서드(boolean 리턴)
        ch_count += 1
    elif ch.isnumeric():
        num_count += 1

if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호 입니다')
else:
    print('불가능한 비밀번호 입니다')