''' <Problem 1>
num = int(input('정수를 입력하세요 >>> '))
if num <= 0:
    print('잘못된 입력입니다.')
else:
    n=1
    while n <= num:
        print('{}번째 Hello'.format(n))
        n += 1
'''

''' <Problem 2>
n=1
while(n<=100):
    if n%7==0: print(n)
    n += 1
'''

''' <Problem 3>
money = int(input('자판기에 얼마를 넣을까요? >>> '))
coffee = 0
if money < 300: print('커피 {}잔, 잔돈 {}원'.format(coffee, money))
while money >= 300:
    money -= 300
    coffee += 1
    print('커피 {}잔, 잔돈 {}원'.format(coffee, money))
'''

''' <Problem 4>
set = set()
while len(set)<5:
    element = int(input('0~9 사이 정수를 입력하세요 >>> '))
    set.add(element)
print('모두 입력되었습니다')
print('입력된 값은 {}입니다.'.format(set))
'''

''' <Problem 5>
tens = 0
units = 1
while tens<=9:
    while units<=10:
        print('%-3d' %(10*tens + units), end='')
        units += 1
    print()
    units = 1
    tens += 1
'''

''' <Problem 6>
dan = 2
n = 1
while dan<=9:
    while n<=9:
        expr = '{}x{}={}'.format(dan, n, dan*n)
        print('%-7s' % expr, end='')
        n +=1
    print()
    n=1
    dan += 1
'''