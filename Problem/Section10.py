''' <Problem 1>
tel = input('전화번호를 입력하세요 >>> ')
telToken = tel.split('-')
print(telToken[1])
'''

''' <Problem 2>
RegiNum = input('사업자등록번호를 입력하세요(예: 123-45-67890) >>> ')
RegiNumCorrect = True

if len(RegiNum) != 3+2+5+2:
    RegiNumCorrect = False

if RegiNum.find('-')!=3 or RegiNum.rfind('-')!=6:
    RegiNumCorrect = False

RegiNumTokenList = RegiNum.split('-')
for RegiNumToken in RegiNumTokenList:
    if RegiNumToken.isdecimal() == False:
        RegiNumCorrect = False

if RegiNumCorrect: print('올바른 형식입니다')
else: print('올바른 형식이 아닙니다')
'''

''' <Problem 3>
print('csv파일 형식으로 학생 이름과 성적을 입력해주세요') # 유효성 검사는 X
csv = input('(예시: "리신",40,"엘리스",70,"그레이브즈",30) >>> ')
csvTokenList = csv.split(',')

for i in range(0, len(csvTokenList), 2): # 0(1)2(3)4(5)...
    name = csvTokenList[i].strip('"')
    score = csvTokenList[i+1] # len(csvTokenList)가 짝수가 아니면 IndexError가 발생
    print('이름은 {}이고, 점수는 {}점입니다'.format(name, score))
'''