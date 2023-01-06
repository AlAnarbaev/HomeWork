# создать файл homework4

# создать 5 классов

# в 2 из них есть конструктор (__init__)
# в одном  атрибут name в другом age

class A:
    def __init__(self, name):
        self.name = name


class B:
    def __init__(self, age):
        self.age = age

# в 2 есть по 1 методу


class C:
    def run(self):
        print("running")


class D:
    def read(self):
        print("reading")

# в последнем классе
# наследовать все классы
# и сделать так чтобы у последнего класса были все методы и атрибуты (name,age)


class E(A, B, C, D):
    def __init__(self, name, age):
        A.__init__(self, name)
        B.__init__(self, age)


h = E('Almaz', '32')
print(h.__dict__)
h.run()
h.read()

