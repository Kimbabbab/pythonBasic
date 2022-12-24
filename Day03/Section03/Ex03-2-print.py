'''

print() 함수 사용법
sep : 출력할 value의 구분 문자
end : value 출력 후 출력할 문자 (기본값 '\n')
file : 출력 방향 지정

'''
print("재미있는", "파이썬")
print("Python", "Java", "C", sep=',') # default: sep = ' '
print("재미있는" + " 자바")

print("안녕", end='') # default: end = '\n'
print("하세요")

# 파일 입출력
fos = open('sample.py', mode='wt') # 같은 디렉토리에 sample.py가 생겼다(메모리 공간에 올라갔다)
# writing text mode
print('print("Hello World")', file=fos)
fos.close()