'''

클래스 변수
    클래스를 기반으로 만든 모든 인스턴스가 공유할 수 있는 변수
    클래스 정의문 바로 아래 대입된 변수
    클래스 객체로부터 참조 가능
    인스턴스 객체로부터 참조 가능
    변경 - 모든 인스턴스의 속성(attribute)을 변경

인스턴스 변수
    그 인스턴스만 사용하는 값
    함수 정의문 바로 아래 대입된 self의 속성(member) 변수
    클래스 객체로부터 참조 불가능
    인스턴스 객체로부터 참조 가능
    변경 - 해당 인스턴스만 속성을 변경

클래스 메소드
    인스턴스가 없어도 클래스를 이용해 호출 할 수 있으며
    cls 이용해 클래스 변수를 사용할 수 있다

'''

class Bag:
    count = 0 # 클래스 변수 / static 변수
    # 인스턴스 변수는 메서드 내에 있다

    def __init__(self):
        Bag.count += 1

    @classmethod # 클래스에 접근이 필요할 때 사용
    def sell(cls):
        cls.count -= 1

    @classmethod # decorator
    def remain_bag(cls):
        return cls.count

    @staticmethod
    def slogan(): # cls 없다 / 클래스에 접근이 필요없을 때 사용
        print('명품 주인을 찾습니다')
        print(Bag.count) # 클래스 멤버에 접근은 가능

print('현재 가방: {}개'.format(Bag.remain_bag()))
bag1 = Bag()
bag2 = Bag()
bag3 = Bag()
print('현재 가방: {}개'.format(Bag.remain_bag()))

print(bag1.count)
print(Bag.count) # 인스턴스가 아닌 클래스명으로 호출
print(bag2.count)
print(bag3.count)

bag1.sell()
Bag.sell() # 인스턴스가 아닌 클래스명으로 호출
print('현재 가방: {}개'.format(Bag.remain_bag()))

bag1.slogan()