with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines() # not readline(), return list
    for no, line in enumerate(line_list):
        print('{}) {}'.format(no+1, line), end='')