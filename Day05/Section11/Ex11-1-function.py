'''
함수(function)
    하나의 특별한 목적의 작업을 수행하기 위해
    독립적으로 설계된 프로그램 코드의 집합
    (객체에 종속되어 있지 않다)
    (C vs Java vs Python or C++)
    (함수 vs 메서드 vs 함수 + 메서드)

def 함수이름(매개변수):
    코드 실행문
    return 반환값

# 매개변수, 반환값은 없을 수도 있다
'''

# welcome() 함수 정의(실행 x)
# 매개변수 x 리턴 x
def welcome():
    print('Hello Python')
    print('Nice to meet you')
    return # 생략 가능

welcome() # 함수 호출(실행)

# 매개변수 o 리턴 x
def introduce(name, age):
    print('내 이름은 {}이고, 나이는 {}살 입니다'.format(name, age))

introduce('james', 25)

def show(*args): # 가변 매개변수(개수를 모름)
    print(type(args)) # tuple로 인자를 받는다
    for item in args:
        print(item)

show('Python')
show('Python', 'Java', 'C')
show(['Python', 'C++']) # 1개의 인자

# 반환(return) 값이 있는 함수
# 매개변수 x 리턴 o
def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

print(address())

# 매개변수 o 리턴 o
def plus(num1, num2):
    return num1 + num2

print(plus(1, 3))
print(plus(2, 5))

area = 0 # 전역변수; 함수에 종속된 지역변수가 아님
def move():
   # area = area + 1 <- error, 전역변수 변경 불가; global area
   # 인터프리터는 area를 move() 함수의 지역변수로 인식; 값이 할당되기 전 사용
    return area + 1

result = move() # 1
print('유닛이 오른쪽으로 {}칸 이동했습니다'.format(result))
print(area) # 0