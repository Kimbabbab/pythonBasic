with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines() # not readline(), return list
    print(line_list)
    for line in line_list:
        print(line, end='')