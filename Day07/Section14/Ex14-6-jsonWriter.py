'''

JSON (JavaScript Object Notation)
    - 딕셔너리 비슷하다
    - 구조
    { K : V }

잡스 형님 -> 아이폰!! -> 대 멀티디바이스 시대!!
-> 모든기기 통신 가능 시대 -> 프로토콜(통신규칙) -> http 시대
-> javascript 시대 -> json 시대
-> xml 시대 끝났다

'''
import json # json package

# 첫 번째 방법
'''
dict_list = [
    {
        'name' : 'james',
        'age' : 20,
        'spec' : [
            175.5,
            70.5
        ]
    },
    {
        'name' : 'alice',
        'age' : 21,
        'spec' : [
            168.5,
            60.5
        ]
    }
]
json_string = json.dump(dict_list)
with open('dictList.json', 'w') as file:
    file.write(json_string)
print('dictList.json 파일이 생성되었습니다')
'''

# 두 번째 방법
dict_list = [
    {
        'name' : 'james',
        'age' : 20,
        'spec' : [
            175.5,
            70.5
        ]
    },
    {
        'name' : '홍길동',
        'age' : 21,
        'spec' : [
            168.5,
            60.5
        ]
    }

]

# indent 들여쓰기, ensure_ascii=False 한글을 아스키코드로 읽지 않는다(깨짐 방지)
json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)
with open('dictList.json', 'w', encoding='UTF-8') as file:
    file.write(json_string)
print('dictList.json 파일이 생성되었습니다')