'''
조건문
    특정 조건을 만족하는지 여부에 따라
    실행하는 코드가 달라야 할 때 사용한다.
    들여쓰기를 사용하여 코드의 범위 정의

    case 1.
    if(조건식):
        (조건식 참) 실행할 코드

    case 2.
    if(조건식):
        (조건식 참) 실행할 코드
    else:
        (조건식 거짓) 실행할 코드

    case 3.
    if(조건식1):
        (조건식1 참) 실행할 코드
    elif(조건식2):
        (조건식2 참) 실행할 코드
    else:
        (조건식 거짓) 실행할 코드
'''

# if(조건식)
a = 7
b = 100
if b > a:
    print("b는 a보다 크다")

# if(조건식) else
a = 7
b = 4
if b >= a:
    print("b는 a보다 크거나 같다")
else:
    print("b는 a보다 작다")

# if(조건식1) elif(조건식2) else
b = 3
if b == 1:
    print("1")
elif b == 2:
    print("2")
elif b == 3:
    print("3")
else: # 필요없으면 생략가능
    print("1,2,3 아니다")