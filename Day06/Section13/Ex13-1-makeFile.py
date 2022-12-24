'''

파일 입출력(I/O - input/output)
    입력(input) 기존 파일 읽어 들이는 것
    출력(output) 파일 생성, 내용 추가를 말한다

'''
file = open('myFile.txt', 'wt') # writing text mode
print('myFile.txt 파일이 생성되었습니다') # (쓰기 모드로)파일을 생성하면 기존의 내용은 사라진다
file.close() # 반드시 스트림을 닫아주자!

# with 문 - 자동으로 close()를 해준다
with open('myFile.txt', 'wt') as file:
    print('myFile.txt 파일이 생성되었습니다')