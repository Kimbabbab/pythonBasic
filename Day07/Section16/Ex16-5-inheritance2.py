'''

다중 상속
죽음의 다이아몬드(A-(B,C)-D)

Python, C++은 다중 상속을 지원하지만 Java는 단일 상속만 지원한다
'''

class A:
    def greeting(self):
        print('안녕하세요 A입니다')
        
class B(A):
    def greeting(self): # 오버라이딩: 부모로 부터 상속받은 메서드를 재정의
        print('안녕하세요 B입니다')

class C(A):
    def greeting(self): # overriding
        print('안녕하세요 C입니다')

class D(B, C): # 다중상속
    pass # 내부동작 필요없고 빈껍데기만 필요할 때

x = D()
x.greeting() # 누구의 greeting인가? 먼저 선언된 B?
print(D.mro()) # 우선순위 출력, 최상위 클래스 object
# Method Resolution Order