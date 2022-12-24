'''

예외처리 세분화

'''
import traceback

try:
    a = int(input('제수를 입력하세요 >>> ')) # '1.5'->1 불가능('1'->1은 가능)
    b = int(input('피제수를 입력하세요 >>> '))
    print('{} / {} = {}'.format(a, b, a / b))
    raise Exception('강제로 발생시킨 예외')
    # Exception 예외 인스턴스 발생
    # 생성자의 인자로 예외 정보를 준다
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')
except ValueError:
    print('정수만 입력할 수 있습니다')
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