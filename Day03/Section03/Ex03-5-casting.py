'''
Casting(형변환)
    변수에 유형을 지정하려는 경우 캐스팅으로 가능
'''
# 정수형
x = int(1)
print(x)

y = int(2.8)
print(y)

z = int("3")
print(z)
print(type(z))

# z = int('A') <- error
# ASCII(0~127 까지 mapping, 1byte = 8bit = 256)
print(ord('A'), ord('a')) # chr(String of length 1) -> int
print(chr(65), chr(97)) # int -> chr

''' str -> int invalid
z = int("ab")
print(z)
'''

# 실수형
x = float(1)
print(x)

z= float("3.3")
print(z)
print(type(z))

# 문자형
x = str(1) # ="1"
y = str(2) # ="2"
print(x)
print(x+y) # ="12"