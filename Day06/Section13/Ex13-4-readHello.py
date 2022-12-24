'''

r (read mode): 읽기 전용 모드 / 파일 없으면 에러

절대경로: 최상위 디렉토리가 포함된 경로
 e.g) C:/Users/JJH/PycharmProjects/pythonProject/Day06/Section13/hello.txt
상대경로: 현재 디렉토리를 기준으로 작성된 경로
 e.g) ../test/test.txt
    ./hello.txt
    ..(상위폴더), .(현재폴더), ''(최상위폴더)
    not \(backslash), use /(forward slash)
'''

# file = open('./hello.txt', 'rt', encoding='UTF-8')
# 절대경로
file = open('C:/Users/JJH/PycharmProjects/pythonProject/Day06/Section13/hello.txt', 'rt', encoding='UTF-8')
str = file.read() # 개행문자 \n 포함
print(str, end='') # Ex13-3에서 'hello.txt'의 마지막에 개행을 했으므로 보기 좋게 바꾸자
file.close()

# 상대경로
with open('../Test/test.txt', 'rt', encoding='UTF-8') as file:
    str = file.read()
    print(str, end='')