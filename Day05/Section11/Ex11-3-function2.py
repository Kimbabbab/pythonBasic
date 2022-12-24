def get_average(marks):
    total = 0
    for subject in marks: # subject <- marks.keys()
        total += marks[subject]
    l_average = total / len(marks) # float
    # marks의 길이는 ,의 개수로 확인(key-value 쌍의 개수)
    return l_average

marks = {
    '국어': 90,
    '영어': 80,
    '수학': 85
}

average = get_average(marks)
print('평균은 {}점 입니다.'.format(average))