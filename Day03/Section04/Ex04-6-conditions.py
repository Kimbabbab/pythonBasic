'''
조건 연산자(삼항 연산자)
    참 if 조건식 else 거짓
    조건식 결과에 따라 참 또는 거짓의 결과를 반환한다

'''
a = 20
b = 10
result = a - b if a >= b else b - a # 간단한 분기처리
print('{}과 {}의 차이는 {}입니다.'.format(a, b, result))