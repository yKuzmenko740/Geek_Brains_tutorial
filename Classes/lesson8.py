# Объекты-свойства (property)
class NoDataDescr:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return "NoDataDescr __get__"


class CoordValue:
    def __set_name__(self, owner, name):  # Задаёт имя автоматически, без функции инит
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point:
    noData = NoDataDescr()
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


p1 = Point(1, 2)
p2 = Point(10, 20)
print(p1.coordX, p1.coordY)
print(p2.coordX, p2.coordY)
p1.noData = 'hello'
