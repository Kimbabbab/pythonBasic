my_list = []
n = 1

while n != 0:
    n = int(input('정수를 입력하세요(종료는 0입니다) >>> '))
    my_list.append(n)

my_list.pop() # 마지막으로 입력받은 0을 제거한다
print(my_list)