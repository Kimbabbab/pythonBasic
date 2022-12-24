'''
for문과 dict
'''

eng_dict = {
    'sun': '태양',
    'moon': '달',
    'star': '별',
    'space': '우주'
}

eng_dict_keys = eng_dict.keys() # list
print(eng_dict_keys)
for word in eng_dict_keys: # word는 eng_dict 객체의 key에 해당
    print('{}의 뜻: {}'.format(word, eng_dict.get(word)))

print(eng_dict)
for word in eng_dict: # 자동으로 key값이 들어간다
    print('{}의 뜻: {}'.format(word, eng_dict.get(word)))