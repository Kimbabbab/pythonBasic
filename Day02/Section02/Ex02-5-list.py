'''
List
    단일 변수에 여러 항목을 저장하는데 사용된다.
    List 항목은 순서가 지정되고 변경 가능하며 중복값 허용
    List 에는 다양한 데이터 유형이 포함될 수 있다.
'''

thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist)
print(thislist[0])
# List 길이
print(len(thislist))

# list 데이터 유형
list1 = ["피카츄", "라이츄", "꼬부기"]
list2 = [1, 2, 3, 5]
list3 = [True, False, False]
# 다양한 유형 포함 가능
list4 = ["abc", 34, False, 40.0]

# 항목 접근
thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist[1])

# 변경
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist[1] = "잠만보"
print(thislist)

# 항목 변경 2개
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울먹이", "메타몽"]
print(thislist)

# 두번째 세번째 값을 하나의 값으로 변경
# element 하나하나 바꾸는게 아니라 통째로 바꾸는 것이다
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울먹이"]
print(thislist)

thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울먹이", "메타몽", "잠만보"]
print(thislist)

# 항목추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.append("꼬부기")
print(thislist)

# 항목추가 - 인덱스번호로 추가
# 1번에 넣고 1번~ element를 뒤로 한칸씩 민다
thislist = ["피카츄", "라이츄", "파이리"]
thislist.insert(1, "잠만보")
print(thislist)

# 항목 값으로 제거
thislist = ["피카츄", "라이츄", "파이리", "라이츄"]
thislist.remove("라이츄") # 최초의 것만 제거한다
print(thislist)

# 항목을 지정된 인덱스로 제거
thislist = ["피카츄", "라이츄", "파이리"]
print(thislist.pop(1)) # pop 메서드는 리스트의 element를 리턴한다
# object(객체)에 종속된 함수를 메서드라고 한다
print(thislist)

# 마지막 값 제거
thislist = ["피카츄", "라이츄", "파이리"]
print(thislist.pop())
print(thislist)

# 목록 삭제
thislist = ["피카츄", "라이츄", "파이리"]
thislist.clear()
print(thislist)

# 확장
thislist = ["피카츄", "라이츄", "파이리"]
thislist.extend(["버터플", "야도란"])
print(thislist)

# 확장2
print(["피카츄", "라이츄", "파이리"] + ["버터플", "야도란"])

# 객체 삭제
del thislist # 메모리상에서 삭제된다(garbage collection)
# print(thislist) // error