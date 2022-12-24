'''
open 함수 모드
    w(write mode): 쓰기 전용 모드 / 파일 없으면 생성
    t(text mode): 해당파일의 데이터를 텍스트 파일로 인식하고 입출력
    b(binary mode): 해당파일의 데이터를 바이너리 파일로 인식하고 입출력(00010101000101...)
     e.g) 이미지, 영상, 음악등은 바이너리 파일로 읽어야 한다
     e.g) 데이터 복사, 전송
'''

file = open('hello.txt', 'wt', encoding='UTF-8') # 현재 파이참의 인코딩 설정을 UTF-8로 했다
# default: x-windows-949
# 메모리상에 hello.txt를 저장한다
file.write('안녕하세요')
file.write('\n')
file.write('반갑습니다')
file.write('\n')
print('hello.txt 파일이 생성되었습니다')
file.close()
# 메모리에서 사라지고 파일로 남는다