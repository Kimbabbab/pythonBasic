'''
finally
    try 절에서 예외 발생여부 관계없이 항상 실행
else
    try 절에서 except 절이 실행되지 않으면 else절 실행

'''

import traceback

try:
    a = float(input('제수를 입력하세요 >>> ')) # '1'->1.0
    b = float(input('피제수를 입력하세요 >>> '))
    print('{} / {} = {}'.format(a, b, a / b))
except ZeroDivisionError:
    print('0.0으로 나눌 수 없습니다')
except ValueError:
    print('실수만 입력할 수 있습니다')
except Exception as e:
    # 예외 정보 출력
    print(e)
    # 예외 상세 정보 출력
    trace_back = traceback.format_exc()
    message = str(e) + '\n' + str(trace_back)
    print(message)
    print('예외가 발생했습니다')
except: # 너무 광범위한 예외 처리
    print('그밖의 에러')
else: # 에러가 나면 실행되지 않음
    print('예외가 발생하지 않을 때 실행, 연산 성공!!')
finally: # 파일 close 등 반드시 실행되야하는 코드
    print('반드시 출력해 주세요!!!!')