dan = 2
while dan <= 9:
    n = 1
    while n <= 9:
        print('{}x{}={}'.format(dan, n, dan * n), end = '|' if n<9 else '')
        n += 1
    dan += 1
    print() # 줄 띄우기