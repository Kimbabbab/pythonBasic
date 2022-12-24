'''

상속
    어떤 클래스가 가지고 있는 기능을
    그대로 물려받아 사용할 수 있는 클래스

상속방법
class 슈퍼클래스:
    본문(구현내용)

class 서브클래스(슈퍼클래스):
    본문(구현내용)

'''

# 슈퍼 클래스
class Coffee:

    price = 2000 # Coffee의 클래스 변수

    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print('원두: {}'.format(self.bean))

# 서브 클래스
class Espresso(Coffee):
    def __init__(self, bean, water):
        su = super() # 부모 클래스 임시 객체 생성
        su.__init__(bean)
        # super().__init__(bean)
        # Python은 반드시 슈퍼 클래스의 생성자를 먼저 호출해야 한다
        # 클래스 멤버와는 다르게 인스턴스 멤버는 자동으로 상속되지 않는다
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print('물: {}ml'.format(self.water))
        print('가격: {}원'.format(super().price)) # 부모 클래스의 클래스 변수에 접근, super.price는 안된다

coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()