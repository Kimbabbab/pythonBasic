'''

CSV(comma-separated values)
    필드를 쉼표(,)로 구분한
    텍스트 데이터 파일이다
    (Excel -> CSV)

'''
student_list = []
with open('학생명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline() # 첫줄 제거
    while True:
        line = file.readline() # str
        if not line:
            break
        student = line.split(',') # ','구분 리스트로 반환
        student_list.append(student) # 리스트 안에 리스트 추가
print(student_list) # 2차원 리스트