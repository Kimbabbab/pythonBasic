'''

예외처리
    프로그램 존재하는 오류 비슷하지만
    개발자가 직접처리 할 수 있는 문제를 예외라고 한다

'''
a = int(input('제수를 입력하세요 >>> '))
b = int(input('피제수를 입력하세요 >>> '))

# 고전적인 예외 처리
if b == 0: print('0으로 나눌 수 없습니다')
else: print('{} / {} = {}'.format(a, b, a / b))
