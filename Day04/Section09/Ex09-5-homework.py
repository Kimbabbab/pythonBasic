'''
[회원가입]
prompt: 아이디를 입력하세요(3글자 이상) >>>
> 3글자 이상 입력해 주세요!

패스워드를 입력하세요(영문 숫자 포함 8자이상) >>>
> 영문 숫자 포함 8자이상 입력해 주세요!

같은 패스워드를 한번 더 입력하세요 >>>
> 일치하지 않습니다, 다시 입력해 주세요!

회원가입 완료!!

[로그인]
아이디를 입력하세요 >>>
> 아이디가 일치하지 않습니다

패스워드를 입력하세요 >>>
> 패스워드가 일치하지 않습니다

로그인 성공!!
(사용자)님 환영합니다 :)

'''

# 아이디 입력
while True:
    id = input('아이디를 입력하세요(3글자 이상) >>> ')
    '''id_count = 0
    for ch in id:
        id_count += 1'''
    
    if len(id)>=3: break
    print('> 3글자 이상 입력해 주세요!')

# 패스워드 입력
while True:
    pw = input('패스워드를 입력하세요(영문 숫자 포함 8자이상) >>> ')
    if len(pw)<8:
        print('> 영문 숫자 포함 8자이상 입력해 주세요!')
        continue

    pw_hasNumber = False
    pw_hasAlphabet = False
    for pw_token in pw: # String of length 1
        if pw_token.isnumeric():
            pw_hasNumber = True
        elif pw_token.isalpha():
            pw_hasAlphabet = True

    # 영문, 숫자 포함 유효성 검사
    if not(pw_hasNumber and pw_hasAlphabet):
        print('> 영문 숫자 포함 8자이상 입력해 주세요!')
        continue

    # 패스워드 확인
    pwCheck = input('같은 패스워드를 한번 더 입력하세요 >>> ')
    if pwCheck != pw:
        print('> 일치하지 않습니다, 다시 입력해 주세요!')
        continue

    break

print('회원가입 완료!!')

# 로그인 아이디
while True:
    loginId = input('아이디를 입력하세요 >>> ')
    if loginId == id:
        break
    print('> 아이디가 일치하지 않습니다')

# 로그인 패스워드
while True:
    loginPw = input('비밀번호를 입력하세요 >>> ')
    if loginPw == pw:
        break
    print('> 비밀번호가 일치하지 않습니다')

print('''로그인 성공!!
{}님 환영합니다 :)'''.format(id))