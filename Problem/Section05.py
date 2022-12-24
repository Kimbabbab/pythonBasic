''' <Problem 1>
score = int(input('점수를 입력하세요 >>> '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print('점수는 {}점이고, 학점은 {}학점입니다'.format(score, grade))
'''

''' <Problem 2>
num = int(input('정수를 입력하세요 >>> '))
if num % 3 ==0:
    print('{}는 3의 배수입니다.'.format(num))
else:
    print('{}는 3의 배수가 아닙니다.'.format(num))
'''

''' <Problem 3>
num1 = int(input('정수1 입력 >>> '))
num2 = int(input('정수2 입력 >>> '))
num3 = int(input('정수3 입력 >>> '))

max = num1
if num2 > max: max = num2
if num3 > max: max = num3
print('가장 큰 수는 {}입니다.'.format(max))
'''

''' <Problem 4>
carNum = input('차량번호를 입력하세요 >>> ')
if int(carNum[-1]) % 2 == 0:
    drivable = '운행가능'
else:
    drivable = '운행불가'
print("차량번호 '{}'는 오늘 {}입니다.".format(carNum, drivable))
'''