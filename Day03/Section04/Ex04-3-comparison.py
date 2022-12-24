'''
관계연산자(비교연산자)
    2개 항을 비교하여 그 결과를 논리(bool) 자료형으로 반환
    e.g) >, >=, <, <=, ==, !=
'''

a = 15
print('{} > 10 : {}'.format(a, a > 10))
print('{} >= 10 : {}'.format(a, a >= 10))
print('{} < 10 : {}'.format(a, a < 10))
print('{} <= 10 : {}'.format(a, a <= 10))
print('{} == 10 : {}'.format(a, a == 10))
print('{} != 10 : {}'.format(a, a != 10))

print('%d > 10 : %s' %(15, 15 > 10)) # True
print('%d > 10 : %d' %(15, 15 > 10)) # 1
