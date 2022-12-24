member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',') # list
        # ['"강나라"', '필라테스', '25일\n']
        member[0] = member[0].strip('"')
        # 큰따옴표(") 제거
        member[2] = member[2].strip('\n')
        # 개행 제거
        member_list.append(member)

print(member_list)