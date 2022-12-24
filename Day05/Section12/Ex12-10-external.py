'''

패키지
    모듈 상위 개념
    모듈의 집합을 의미한다

다른 디렉토리에 있는 파이썬 파일에는 접근할 수 없다
패키지화 시키면 패키지.모듈... 으로 접근할 수 있다

패키지 설치; 파이썬에서 제공해주는 오픈소스 서버가 있다
console> pip install package명

패키지 삭제
console> pip uninstall package명

'''

# cmd> pip install numpy

# 행렬 연산 관련 package
import numpy as np

print(np.sum([1,2,3,4,5]))

a = np.array([1,2,3]) # 1차원 matrix(vector)
b = np.array([4,5,6])

# 각 요소 더하기
c = a + b
print(c)
print(np.add(a, b))

# 각 요소 빼기
c = a - b
print(c)
print(np.subtract(a, b))

# 각 요소 곱하기
c = a * b
print(c)
print(np.multiply(a, b))

# 각 요소 나누기
c = a / b
print(c)
print(np.divide(a, b))