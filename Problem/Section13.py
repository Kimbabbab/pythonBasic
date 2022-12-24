''' <Problem 1>
nation = ['그리스', '아테네', '독일', '베를린', '러시아', '모스크바', '미국', '워싱턴']

with open('nation.txt', 'wt', encoding='UTF-8') as file:
    for i in range(0, len(nation), 2): # 짝수번 인덱스, 나라 이름
        file.write('{}-{}\n'.format(nation[i], nation[i+1]))
print("'nation.txt' 파일이 생성 되었습니다")
'''

''' <Problem 2>
file = open('연락처.txt', 'rt', encoding='UTF-8')
str = file.read() # 하나의 문자열
print(str)
print('총 {}건의 011 데이터를 찾았습니다'.format(str.count('011')))
file.close()

with open('연락처.txt', 'wt', encoding='UTF-8') as file:
  # str = file.read() # 'wt'이기 때문에 read() 메서드를 쓸 수 없다
    str = str.replace('011', '010')
    file.write(str)
    print('모든 데이터를 수정했습니다')
    print(str)
'''