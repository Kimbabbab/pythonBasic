'''

지역변수(local)
    함수 내부 선언
    함수 내부에서만 사용 가능
    
전역변수(global)
    함수 외부 선언
    함수 내부 외부 모두 사용 가능

'''

gVar = 'global' # 전역변수
def globalAndLocal():
    lVar = 'local' # 지역변수
    print(gVar, 'variable') # 전역변수; 참조만 하고 있다, 함수내 변경 불가!
    print(lVar, 'variable')

globalAndLocal()

def globalAndLocal(): # globalAndLocal() 함수를 새롭게 정의
    lVar = 'local'
    gVar = 'not global, new local' # 새롭게 선언된 지역변수
    print(gVar, 'variable')
    print(lVar, 'variable')
    print(id(gVar))

globalAndLocal()
print(gVar) # 위에서 선언된 전역변수가 출력된다
print(id(gVar)) # 전역변수의 아이디값

print()
# 전역변수 선언
total = 0
def gift(dic, who, money):
   # total = -1 <- error, global 키워드로 가져온 전역변수는 global 이전에 지역변수로 쓸 수 없다
    global total # 전역변수 total를 사용하겠다(값 변경 권한 부여)
    total += money
    dic[who] = money # mutable dic을 매개변수로 받았다, 함수 내의 동작이 바깥에 영향을 준다
   # dic(mutable), who/money(immutable)

wedding = {} # empty dictionary
gift(wedding, '영희', 50_000) # total += 50_000
gift(wedding, '철수', 60_000) # total += 60_000
gift(wedding, '이모', 100_000) # total += 100_000
print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))

def increase(n):
    n += 1 # 매개변수(지역변수) n
    return n

n = 2 # immutable value이므로 값이 변하면 객체가 다른 주소를 참조한다
# 따라서 함수내의 동작이 바깥에 영향을 미치지 않는다
# 처음엔 전역변수 n과 지역변수 n이 같은 2를 참조하다(Python의 모든 변수는 객체다)
# 함수의 동작중 지역변수 n은 3을 참조하고, 전역변수 n은 그대로 2를 참조한다

increase(n)
print(n) # 2

n = increase(n)
print(n) # 3