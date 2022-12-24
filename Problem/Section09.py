''' <Problem 1>
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
# method1
for item in enumerate(rainbow): # item is tuple(index, element)
    print('무지개의 {}번째 색은 {}입니다'.format(item[0]+1, item[1]))
# method2
for index, element in enumerate(rainbow): # unpacking
    print('무지개의 {}번째 색은 {}입니다'.format(index +1, element))
'''

''' <Problem 2>
print('점수를 입력하세요. 더 이상 입력할 점수가 없으면 음수를 아무거나 입력하세요.')
exam = []
sum = 0
while True:
    score = int(input('점수 입력 >>> '))
    if score<0: break
    exam.append(score)
    sum += score
avg = sum / len(exam)
print('평균 = {}, 최대 = {}, 최소 = {}'.format(avg, max(exam), min(exam)))
'''