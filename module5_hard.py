import time


class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video:

    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.time_now = time_now
        self.adult_mode = adult_mode
        self.title = title
        self.duration = duration

    def __eq__(self, other):
        if other == self.title:
          return self.title == Video

    def __contains__(self, item):
        return item in self.title

class  UrTube:

    users = []
    videos = []
    current_user = None

    def log_in(self, login: str, password: str):
        for user in self.users:
          if login == user.nickname and password == user.password:
             self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        new_user = User(nickname, password,age)
        self.users.append(new_user)
        self.current_user = new_user


    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for movie in args:
            if len(self.videos) == 0:
                self.videos.append(movie)
            else:
                for i in range(0, len(self.videos)):
                    if ur.videos[i].title == movie.title:
                        print()
                    else:
                        self.videos.append(movie)

    def get_videos(self, text: str):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for x in self.videos:
            if x.title == movie:
                if x.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return

                for i in range(1, 11):
                    print(i, end='')
                    x.time_now += 1
                x.time_now = 0
                print('Конец видео')

if __name__ == '__main__':


    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
