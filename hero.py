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
    #
    def __str__(self):
        return (f'Nickname: {self.nickname} \nSuperpower: {self.superpower} \nHealth: {self.health_points} HP')

    # 6) создать магический метод который считает длину коронной фразы героя

    def __len__(self):
        return len(self.catchphrase)

hero1 = SuperHero(name = 'Bruce Banner', nickname='Hulk',superpower='Superpower',health_points=100,catchphrase='Hulk smash!')

hero1.show_hero_name()
hero1.double_health_points()
print(hero1)
print(f'Catchphrase lenght: {hero1.__len__()}')


# Создаем новый класс, наследованный от основного
class AirElement(SuperHero):

    # Создаем аттрибут класса

    element = 'air'

    # Создаем конструктор класса, добавляем новый параметр fly и даем значение по умолчанию False

    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly

    # Изменяем метод double_health_points() (теперь он должен возводить его в квадрат и меняет значение параметра fly на True)

    def double_health_points(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    # Создаем новый метод который выводит фразу fly in the True_phrase

    def fly_method(self):
        print("fly in the True_phrase")

# Создаем новый класс, наследованный от основного

class EarthElement(SuperHero):

    # Создаем аттрибут класса

    element = 'earth'

    # Создаем конструктор класса, добавляем новый параметр fly и даем значение по умолчанию False

    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly

    # Изменяем метод double_health_points() (теперь он должен возводить его в квадрат и меняет значение параметра fly на True)

    def double_health_points(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    # Создаем новый метод который выводит фразу fly in the True_phrase

    def fly_method(self):
        print("fly in the True_phrase")


# Создаем новый класс, наследованный от основного
class SpaceElement(SuperHero):

    # Создаем аттрибут класса

    element = 'space'

    # Создаем конструктор класса, добавляем новый параметр fly и даем значение по умолчанию False

    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly

    # Изменяем метод double_health_points() (теперь он должен возводить его в квадрат и меняет значение параметра fly на True)

    def double_health_points(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    # Создаем новый метод который выводит фразу fly in the True_phrase

    def fly_method(self):
        print("fly in the True_phrase")

# Cоздаем объекты новых наследованных классов

ironman = AirElement(name = 'Tony Stark', nickname = 'Iron man', superpower = 'Superhuman intellect', health_points = 100, catchphrase = 'I am Iron Man', fly = False)
cpt_america = EarthElement(name = 'Steve Rogers', nickname = 'The Captain America', superpower = 'Superhuman durability', health_points = 150, catchphrase = 'I can do this all day', fly = False)
thanos = SpaceElement(name = 'Thanos', nickname='The Mad Titan',superpower='Superstrenght',health_points=200,catchphrase='I am inevitable', fly = False)

# Вызываем новые методы

ironman.double_health_points()
cpt_america.double_health_points()
thanos.double_health_points()

ironman.fly_method()
cpt_america.fly_method()
thanos.fly_method()

print(ironman.__dict__)
print(cpt_america.__dict__)
print(thanos.__dict__)
