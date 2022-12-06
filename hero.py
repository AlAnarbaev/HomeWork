# создать новый проект HomeWork
# создать файл hero.py

# 1) создать класс SuperHero с атрибутом класса people='people'

class SuperHero:

    people = 'people'

    # 2) создать конструктор класса с атрибутами name,nickname,superpower,health_points, catchphrase.

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    # 3) добавить метод, который выводит имя героя

    def show_hero_name(self):
        print(self.name)

    # 4) добавить метод который умножает здоровье героя на 2

    def double_health_points(self):
        self.health_points = self.health_points * 2

    # 5) добавить магический метод, который выводит прозвище героя, его суперспособность и его здоровье

    def __str__(self):
        print(f'Прозвище героя: {self.nickname} \nSuperpower: {self.superpower} \nЗдоровье {self.health_points} HP')
    # 6) создать магический метод который считает длину коронной фразы героя

    def count_catchphrase_lenght (self):
        return len(self.catchphrase)

# 7) создать объект класса Hero и вызвать все методы которые вы создали

hero1 = SuperHero('Bruce Banner','Hulk','Superpower',100,'Hulk smash!')

hero1.show_hero_name()
hero1.double_health_points()
hero1.__str__()
print(hero1.count_catchphrase_lenght())

# 8) скачать гитхаб и зарегистрироваться там

# 9) создать репозиторий и привязать его с вашим проектом

# 10) запушить проект в репозиторий и отправить мне ссылку на него