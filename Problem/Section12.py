''' <Problem 1>
import time
import random

pot = [n for n in range(1,46)] # 1~45
jackpot = []
for i in range(1,7): # 1~6
    random.shuffle(pot)
    lottoNum = pot.pop() # pot에서 lottoNum이 제거 되었으므로 중복은 발생하지 않는다
    jackpot.append(lottoNum)
    print('{}번째 당첨번호는 {}입니다'.format(i, lottoNum))
    time.sleep(1)
jackpot.sort(reverse=False) # 오름차순 정렬
print(jackpot)
'''

''' <Problem 2>
import random
import time
import math

print('UpDown게임을 시작합니다')
answer = random.randint(1,100)

start = time.time() # 1970년 1월 1일부터 현재까지 경과한 시간
while True:
    user = int(input('어떤 값일 까요? >>> '))
    if answer > user:
        print('Up')
    elif answer < user:
        print('Down')
    else:
        print('정답입니다')
        break
end = time.time()
elapse = end - start
elapse = math.trunc(elapse) # 소수점 제거
print('{}초 만에 성공했습니다'.format(elapse))
'''