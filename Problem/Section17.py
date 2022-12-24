''' <Problem 1>
class Quiz:
    answer = ['경기도', '강원도', '충청남도', '충청북도', '전라남도',
              '전라북도', '경상남도', '경상북도', '제주특별자치도']

    @classmethod
    def challenge(cls):
        user = input('정답은? >> ')
        if user in cls.answer:
            cls.answer.remove(user)
            print('정답입니다')
        else: raise Exception('틀렸습니다')

        if cls.answer != []:
            cls.challenge() # recursive call
        else: print('모든 도를 맞혔습니다. 성공입니다')


try:
    print('우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요')
    Quiz.challenge()
except Exception as e: # 오답시 즉시 종료
    print(e)
'''

''' <Problem 2>
import random

class UpDown:
    def __init__(self):
        self.answer = random.randint(1,100)
        self.count = 0

    def play(self):
        while True:
            user = self.challenge()
            if user == -1: continue
            if user > self.answer:
                print('Down!')
            elif user < self.answer:
                print('Up!')
            else:
                print('{}번만의 정답입니다'.format(self.count))
                break

    def challenge(self): # 사용자 입력값을 리턴(잘못된 입력은 -1)
        try:
            user = int(input('입력(1~100) >> '))
            if user < 1 or user > 100:
                raise Exception('1~100 사이만 입력하세요')
            return user
        except Exception as e:
            print(e)
            return -1
        finally:
            self.count += 1 # return 이전에 실행된다

game = UpDown()
game.play()
'''

''' <Problem 3>
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, money):
        try:
            if money < 0: raise BankError('{}원 입금 불가'.format(money))
            self.balance += money
        except BankError as e:
            print(e)

    def withdraw(self, money):
        try:
            if money < 0: raise BankError('{}원 출금 불가'.format(money))
            if money > self.balance: raise BankError('잔액 부족')
            self.balance -= money
        except BankError as e:
            print(e)
            money = 0 # 금액을 출금하지 못했다
        return money

    def transfer(self, your_acc, money):
        your_acc.deposit(self.withdraw(money))
        # 먼저 나의 계좌에서 출금을 진행한다, 실패시 0원을 출금
        # 출금한 돈을 상대방의 계좌에 입금한다

    def inquiry(self):
        print('계좌번호: {}'.format(self.acc_no))
        print('통장 잔액: {}'.format(self.balance))

class BankError(Exception): # custom(user-defined) exception
    def __init__(self, message):
        super().__init__(message)

# main
me = BankAccount('012-34-56789', 50000)
you = BankAccount('987-65-43210', 50000)

while True:
    print('<< 계좌 관리 프로그램 >>')
    menu_dict = {1: '입금', 2: '출금', 3: '이체', 4: '조회(me)', 5: '조회(you)', 6: '종료'}
    print(menu_dict)
    try:
        menu = int(input('메뉴 번호 입력 >> '))
        if menu < 1 or menu > 6: raise ValueError()
    except ValueError:
        print('메뉴 번호는 1에서 6사이의 정수로 입력하세요')
        continue

    if menu == 1:
        money = int(input('입금할 금액 입력 >> '))
        me.deposit(money)
    elif menu == 2:
        money = int(input('출금할 금액 입력 >> '))
        me.withdraw(money)
    elif menu == 3:
        money = int(input('이체할 금액 입력 >> '))
        me.transfer(you, money)
    elif menu == 4:
        me.inquiry()
    elif menu == 5:
        you.inquiry()
    else: break
'''