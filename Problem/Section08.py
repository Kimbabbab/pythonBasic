''' <Problem 1>
balance = 10000
while True:
    print('현재 {}원이 있습니다'.format(balance))
    if balance == 0: break
    pay = int(input('사용할 금액 입력 >>> '))
    if pay <= 0:
        print('0이하의 금액은 사용할 수 없습니다')
        continue
    if pay > balance:
        print('{}원이 부족합니다.'.format(pay-balance))
        continue
    balance -= pay
'''

''' <Problem 2>
while True:
    rating = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if 1<=rating and rating<=5: break
    print('평점은 1~5 사이만 입력할 수 있습니다')
for i in range(1,rating +1):
    print('★', end='') # 'ㅁ' + 한자키
'''

''' <Problem 3>
answer = 'qwerty'
count = 0
while True:
    user = input('비밀번호를 입력하세요 >>> ')
    count += 1
    if user == answer:
        print('비밀번호를 맞혔습니다')
        break
    if count>=5:
        print('비밀번호 입력 횟수를 초과했습니다')
        break
'''

''' <Problem 4>
dan = 2
n = 1
while dan<=9:
    if dan%2 == 0:
        if dan!=2: print()
        dan += 1
        continue # outer loop
    while n<=dan:
        expr = '{}x{}={}'.format(dan, n, dan*n)
        if n==9:
            print(expr, end='')
            break # inner loop(dan==9)
        print(expr)
        n += 1
    n = 1
    dan += 1
'''