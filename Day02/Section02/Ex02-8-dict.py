'''

Dictionary
key:value로 이루어져 쌍으로 데이터 값을 저장하는데 사용
key 이름을 사용하여 참조할 수 있다
dictionary는 key의 중복을 허용하지 않는다
'''

# Dictionary 선언
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : [1999, 2021] # value값으로 list나 dictionary 등도 사용 가능(1개의 키에 여러개의 값)
}
print(thisdict)

# 값 가져오기
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : [1999, 2021]
}
print(thisdict["brand"]) # index "brand"
print(thisdict.get("year"))

# 키 목록 가져오기
print(thisdict.keys()) # list로 반환

# 추가하기
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict.update({"bgColor" : "black"})
print(thisdict)

# 변경하기
thisdict["color"] = "blue"
print(thisdict)

# 제거하기
thisdict.pop("model")
print(thisdict)

# 마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict)