'''

매직 메서드(Magic Method)
    매직 메서드 혹은 스페셜메서드라고 불리며,
    메서드의 양쪽을 두 개의 언더스코어(__)로
    감싼 메서드를 말한다
    
'''

'''
__init__()
생성자
인스턴스를 생성할 때 자동으로 호출
일반적으로 인스턴스 변수를 선언하기 위해 사용된다
'''

class Person1:
    def __init__(self):
        print('인스턴스 생성')
        
p1 = Person1()

'''
__str__()
해당 메서드는 객체를 우리가 이해할 수 있는
문자열로 만들 수 있도록 해준다
'''

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person2('James', 27)
print(p2)
print(p2.__str__())

class Person3: # object의 __str__ 오버라이딩 후
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + ' ' + str(self.age)

p3 = Person3('James', 27)
print(p3)

'''
__len__()
객체의 길이를 구하는 매직메소드
새로 만드는 객체에 대하여 오버라이딩이 가능
'''

class Person4: # object의 __len__ 오버라이딩 후
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __len__(self):
        return self.age

p4 = Person4('James', 27)
print(p4.__len__())
print(len(p4)) # len() 함수 내부에서 __len__() 메서드를 호출한다