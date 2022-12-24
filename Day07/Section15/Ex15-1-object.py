'''

클래스
    객체를 만드는 설계도
    붕어빵 틀, 와플 기계
    인스턴스화 - 메모리에 올리는 것

객체(object)
    현실 세계 존재 하는 물리적, 추상적 식별할 수 있는 모든 것
    ex) 컴퓨터, 학생, 주문, 배송

객체 구성
    생성자 - 초기화용
    속성 값 - 변수
    기능 - 메서드(함수)

'''

# Computer 클래스 정의
class Computer:
    
    # 첫번째 매개변수가 self 이므로 인스턴스 메소드이다
    # self를 제외한 나머지 매개변수에 실제로 사용될 데이터가 전달된다
    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        # self.cpu: 멤버 변수, cpu: 지역 변수
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))
        return

# 객체 생성
desktop = Computer()
desktop.set_spec('i7', '16GB', 'GTX3060', '512GB')
desktop.hardware_info()
print()

desktop.cpu = 'i9'
desktop.hardware_info()
print()

macbook = Computer()
macbook.set_spec('M2', '16GB', 'M2', '512GB')
macbook.hardware_info()
print()

print(id(desktop)==id(macbook)) # False 같은 클래스지만 다른 객체
# call by reference, 주소값으로 값을 호출 : id() 함수