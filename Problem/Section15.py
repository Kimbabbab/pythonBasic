''' <Problem 1>
class Book:
    def set_info(self, name, author):
        self.name = name
        self.author = author
    def print_info(self):
        print('책 제목: {}'.format(self.name))
        print('책 저자: {}'.format(self.author))

book1 = Book()
book2 = Book()
book1.set_info('파이썬', '민경태')
book2.set_info('어린왕자', '생텍쥐페리')
book1.print_info()
book2.print_info()
'''

''' <Problem 2>
class Watch:
    def set_watch(self):
        watch = input("시간을 입력하세요('HH:mm:ss') >> ") # 메서드 내에서 입력받음
        self.hour = int(watch[:2]) % 24
        self.minute = int(watch[3:5]) % 60
        self.second = int(watch[6:]) % 60

    def add_hour(self, hour): # 입력받은 값을 메서드에 전달
        self.hour = (self.hour + hour) % 24 # 0~23

    def add_minute(self, minute):
        hour = (self.minute + minute) // 60
        self.add_hour(hour)  # update hour
        self.minute = (self.minute + minute) % 60 # 0~59

    def add_second(self, second):
        minute = (self.second + second) // 60
        self.add_minute(minute) # update hour, minute
        self.second = (self.second + second) % 60  # 0~59

watch = Watch()
watch.set_watch()
print('현재 시각은 {}시 {}분 {}초 입니다'.format(watch.hour, watch.minute, watch.second))

hour = int(input('계산할 시간을 입력하세요 >> '))
watch.add_hour(hour)
print('계산된 시각은 {}시 {}분 {}초 입니다'.format(watch.hour, watch.minute, watch.second))

minute = int(input('계산할 분을 입력하세요 >> '))
watch.add_minute(minute)
print('계산된 시각은 {}시 {}분 {}초 입니다'.format(watch.hour, watch.minute, watch.second))

second = int(input('계산할 초를 입력하세요 >> '))
watch.add_second(second)
print('계산된 시각은 {}시 {}분 {}초 입니다'.format(watch.hour, watch.minute, watch.second))
'''

''' <Problem 3>
class Song:
    def set_song(self, name, genre):
        self.name = name
        self.genre = genre

    def print_song(self):
        print('노래제목: {}({})'.format(self.name, self.genre))

class Singer:
    def set_singer(self, name):
        self.name = name

    def hit_song(self, song): # 매개변수로 Song 인스턴스를 받음
        self.song = song

    def print_singer(self):
        print('가수이름: {}'.format(self.name))
        self.song.print_song() # Song 인스턴스의 print_song() 메서드

song = Song()
song.set_song('취중진담', '발라드')

singer = Singer()
singer.set_singer('김동률')
singer.hit_song(song)
singer.print_singer()
'''