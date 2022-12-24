# 교집합 intersection()
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 & s2)

print(s1 and s2) # 안된다(잘못된 결과)
result = s1.intersection(s2)
print(result)
print(s2.intersection(s1))

print()
# 합집합
s1 = {"apple", "banana", "cherry"}
s2 = {'apple', 'banana', 'orange'}
print(s1 | s2)

result = s1.union(s2)
print(result)
print(s2.union(s1))

print()
# 차집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 - s2)

result = s1.difference(s2)
print(result)
print(s2.difference(s1)) # print(s2 - s1)