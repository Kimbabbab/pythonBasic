'''

소멸자
    인스턴스가 소멸될 때 자동으로 호출된다
'''

class Service:
    def __init__(self, service):
        self.service = service
        print('{} Service가 시작되었습니다'.format(self.service))

    def __del__(self):
        print('{} Service가 종료되었습니다'.format(self.service))

s = Service('길 안내')
del s
s2 = Service(None)
print("프로그램 종료!")
# 프로그램이 종료되면 메모리 상의 객체들은 자동으로 소멸한다