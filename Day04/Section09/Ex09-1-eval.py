'''

eval() 함수
    매개변수로 받은 expression(식)을
    문자열로 받아서 실행하는 함수
'''
expr = input('계산식을 입력하세요 >>> ') # String
result = eval(expr)
print(expr + '=' + str(result))
# print(expr + '=' + result) // 컴파일 에러, 자동 변환 불가능