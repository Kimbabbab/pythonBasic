'''
for 문과 range 함수

range()
    연속된 숫자를 만들어주는 함수

range(stop): 0 ~ stop -1
range(start, stop): start ~ stop -1
range(start, stop, step)
'''

dan = int(input('출력할 구구단을 입력하세요 >> '))
for n in range(1, 10, 3): # step = 3) 1 4 7
    print('%d x %d = %d' %(dan, n, dan * n))
    # print('{} x {} = {}'.format(dan, n, dan * n))

print(type(range(10))) # class range
print(type([])) # class list