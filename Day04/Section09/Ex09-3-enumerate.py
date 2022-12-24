'''
enumerate() # 열거형
    list, tuple, String 등 자료형을 입력받으면
    인덱스 값을 포함하는 enumerate 객체를 돌려준다
'''

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(type(enumerate(months)))
'''
index value
0 -> 31
1 -> 28
2 -> 31
'''

for month, day in enumerate(months): # index, value
    print('{}월 = {}일'.format(month +1, day))

set = {2, 1, 3}
print(type(enumerate(set)))
for index, value in enumerate(set):
    print('index %d, value %d' %(index +1, value))