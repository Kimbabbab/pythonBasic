import sys # 운영체제에 대한 정보를 가지고 있는 모듈

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines() # not readline(), return list
    sys.stdout.writelines(line_list)