'''

mutable - 메모리 값을(!=주소) 변경 가능한 객체(변수)
 - e.g) 리스트(list), 세트(set), 딕셔너리(dict)
 
 # 메모리 값; 메모리 주소에 저장된 값
 # 매개변수도 함수 내에서 지역변수다
 def 함수(num, str, my_list):
    소스 코드
'''

me = [1,2,3]
print(id(me)) # list 객체에 부여된 고유번호(!= 메모리 주소값)
me.append(4)
print(id(me)) # 메모리 주소는 그대로

'''

immutable - 메모리 값 변경 불가
 - e.g) 정수(int), 실수(float), 문자열(str), 튜플(tuple)
 - 자주 쓰는 값이므로 코드상에서 메모리 주소를 재활용
'''

me = 10
print(id(me))
me += 1 # me = me + 1
print(id(me)) # me 객체가 참조하는 메모리 주소가 바꼈다
# 10을 참조하다가 다른 객체 11을 참조한다(class int)

'''
code area; 소스 코드에 대한 정보
data area; 전역 변수 / 정적(클래스) 변수
stack area; 호출될 함수가 쌓임(메인 함수) // 컴파일 타임에 크기가 결정됨
heap area; 인스턴스가 저장(사용자의 동적 할당) // 런타임에 크기가 결정됨

(code area)
num = 10
str = "hello"
my_list = [1,2,3,4,5]

num = 15
str = "hello world"
my_list.append(6)
my_function()

(stack area) ; LIFO; 마지막에 스택에 들어온 함수부터 호출한다
my_function()
my_list (->[1,2,3,4,5])
str (->"hello"->"hello world")
num (->10->15); immutable, 참조하는 객체가 달라진다

(heap area) ; 순서 없음
10
"hello"
[1,2,3,4,5]->[1,2,3,4,5,6]; mutable, heap area내에서 변경
15
"hello world"

'''