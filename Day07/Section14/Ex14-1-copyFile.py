'''

파일복사
    원본 -> 버퍼 변수(Memory) -> 복사본

'''

buffer_size = 1024 # 1024Byte로 1KB 의미
with open('hello.txt', 'rb') as source: # 텍스트로 복사하면 인코딩 문제가 발생 할 수 있음
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size) # 1024Byte 단위로 읽기
            if not buffer: # 더 이상 read() 메서드로 읽어올 source의 데이터가 없다
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사되었습니다')