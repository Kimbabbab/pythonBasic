'''
예외처리 방법

try:
    코드 작성 영역
except:
    예외 발생시 처리 영역
'''

try:
    a = int(input('제수를 입력하세요 >>> '))
    b = int(input('피제수를 입력하세요 >>> '))
    print('{} / {} = {}'.format(a, b, a / b))
except: # 만약 정수 대신 문자열을 입력한다면?
    print('0으로 나눌 수 없습니다')