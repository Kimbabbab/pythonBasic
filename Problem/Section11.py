''' <Problem 1>
def vending_machine(money):
    price = 700
    drink = money // 700
    change = money

    for i in range(drink +1): # 0~drink
        print('음료수 = {}개, 잔돈 = {}원'.format(i, change))
        change -= 700

vending_machine(3000)
'''

''' <Problem 2>
def get_average(marks):
    sum = 0
    for key in marks:
        value = marks[key]
        sum += value
    return sum / (len(marks))

marks = {
    '국어' : 90,
    '영어' : 80,
    '수학' : 85
}
average = get_average(marks)
print('평균은 {}점입니다'.format(average))
'''

''' <Problem 3>
total = 0
def gift(dic, who, money): # dict, str, int
    global total
    dic[who] = money
    total += money

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)
print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))
'''