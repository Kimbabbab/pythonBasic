'''

readline()
    파일에서 1줄을 읽고 그 결과를 리턴
'''

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    while True:
        str = file.readline() # 줄의 마지막엔 개행문자 /n이 있다
        if str == '': # if not str:
            break
        print(str, end='')