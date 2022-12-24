'''
a (append mode): 추가 모드
쓰기 모드는 기존의 데이터를 삭제하고 다시 쓰는 것이지만
추가 모드는 기존의 데이터는 보존하고 추가로 쓰는 것이다
'''

file = open('hello.txt', 'at', encoding='UTF-8')
file.write('Hello\n')
file.write('Nice to meet you\n')
print('hello.txt 파일에 새로운 내용이 추가 되었습니다')
file.close()