''' <Problem 1>
for i in range(10,5): print(i) # 결과 없음
for i in range(5,0,-1):
    print(i)
'''

''' <Problem 2>
num = int(input('임의의 양수를 입력하세요 >>> '))
sum = 0
for i in range(1, num+1):
    sum += i
print('1부터 {}사이 모든 정수의 합계는 {}입니다'.format(num, sum))
'''

''' <Problem 3>
num = int(input('몇 개의 과일을 보관할까요? >>> '))
basket = []
for i in range(1, num+1):
    item = input('{}번째 과일을 입력하세요 >>> '.format(i))
    basket.append(item)
print('입력받은 과일들은 {}입니다.'.format(basket))
'''

''' <Problem 4>
exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = [min(100,n+5) for n in exam] # list comprehension
print(score)
'''

''' <Problem 5>
pivot = [3,6,9] # 0은 3의 배수지만 369 게임의 조건을 만족시키지 않는다
for i in range(1, 100):
    units = i % 10
    tens = i // 10
    if units in pivot:
        if tens in pivot: result = '짝짝' # case1
        elif tens not in pivot : result = '짝' # case2
    elif units not in pivot:
        if tens in pivot: result = '짝' # case3
        elif tens not in pivot: result = i # case4
    str = ' ' if i%10!=0 else '\n'
    print(result, end=str)
'''