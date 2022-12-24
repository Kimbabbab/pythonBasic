'''

추상 메서드(Abstract Method)
    선언만하고 구현되지 않은 미완성 메서드

추상 클래스(Abstract Class)
    추상 메서드를 하나 이상 가지고 있는 클래스

오버라이딩
    서브 클래스에서 슈퍼 클래스 메서드 재정의

'''
# from abc import *
from abc import ABCMeta # class
from abc import abstractmethod # field(member)

class Family(metaclass=ABCMeta): # ABCMeta 클래스 상속
    @abstractmethod
    def introduce(self):
        pass

class Person(Family): # Family의 추상 메서드를 구현해야 한다
    def introduce(self): # 오버라이딩
        print('저는 사람입니다')

a = Person()
a.introduce()