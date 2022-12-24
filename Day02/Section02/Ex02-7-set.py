'''
set
    순서가 없다
    변경할 수 없다
    인덱싱되지 않는 컬렉션(자료구조)
    중복값 없다
'''

thisset = {"피카츄", "라이츄", "파이리"}
print(thisset) # 실행할 때 마다 순서가 random하다

# 항목 가져오기
for x in thisset: # 값이 없을 때(False)까지 가져온다
    print(x)

# 값이 있는지 확인
print("피카츄" in thisset)
print("꼬부기" in thisset)

# 항목 추가하기
thisset.add("꼬부기") # random하게 추가
print(thisset)

# 다른 set 항목 추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "라이츄"}
thisset1.update(thisset2) # set은 중복값을 허용하지 않는다
print(thisset1)

# 항목 제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
# thisset.remove("피카츄") // error: 없는 항목은 삭제 불가능

thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)
thisset.discard("피카츄")
print(thisset)

# 항목제거
print(thisset.pop()) # 무작위 추출
print(thisset)

# 비우기
thisset.clear()
print(thisset)