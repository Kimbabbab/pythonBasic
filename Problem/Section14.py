''' <Problem 1>
source_name = input('복사할 파일명을 입력하세요 >>> ')
index = source_name.rfind('.')
if source_name[index:]!='.txt':
    print('복사할 수 없는 파일 입니다')
else:
    copy_name = '복사본-' + source_name
    buffer_size = 1024
    with open(source_name, 'rb') as source:
        with open(copy_name, 'wb') as copy:
            while True:
                buffer = source.read(buffer_size)
                copy.write(buffer)
                if not buffer:
                    break
    print('{} 파일이 생성되었습니다'.format(copy_name))
'''

''' <Problem 2>
import csv

cctv_num = 0
with open('cctv.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=',')
    is_first = True
    for line in csv_reader:
        if not is_first: cctv_num += int(line[4].strip())
        else: is_first = False
print('서울특별시 마포구에 설치된 CCTV는 총 {}대입니다'.format(cctv_num))
'''

''' <Problem 3>
import json
with open('cctv.json', 'r', encoding='UTF-8') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)
set = set()
for dict in dict_list:
    for key in dict:
        if key == '설치목적구분':
            value = dict[key]
            set.add(value)
print(set)
'''