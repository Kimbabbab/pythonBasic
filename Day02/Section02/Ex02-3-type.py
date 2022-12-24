'''
내장 데이터 유형
    Python 변수는 다른 유형의 데이터를 저장할 수 있으며
    다른 유형은 다른 작업을 수행할 수 있다.

(Python은 모든 데이터가 참조 데이터 타입이다)
(모든 변수는 인스턴스를 참조한다)
(None은 변수가 어떤 인스턴스도 참조하지 않는 상태다)

텍스트 유형: str
숫자 유형: int, float, complex
시퀀스 유형: list, tuple, range
매핑 유형: dict
세트 유형: set
부울(논리) 유형: bool
바이너리 유형: bytes, bytearray
없음 유형: NoneType

'''

# 텍스트 유형
# str
x = "Hello World"
print(type(x))

# 숫자 유형
# int
x = 20
print(type(x))
# float
x = 20.5
print(type(x))
# complex
x = 1j
print(type(x))

# 시퀀스 유형
# list
x = ["피카츄", "라이츄", "파이리"]
print(type(x))
# tuple
x = ("피카츄", "라이츄", "파이리")
print(type(x))
# range
x = range(6)
print(type(x))

# 매핑 유형
# dict
x = {"name": "피카츄", "기술": "백만볼트!"}

# 세트 유형
# set
x = {"피카츄", "라이츄", "파이리"}
print(type(x))

# 부울(논리) 유형
x = True
print(type(x))

# 없음 유형
x = None
print(type(x))