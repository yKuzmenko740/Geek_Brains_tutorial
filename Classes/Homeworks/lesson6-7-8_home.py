# 1. Объявите класс Calendar для хранения даты: день, месяц, год. Определите свойства для записи и считывания этой
# информации из этого класса. (Дополнение: используя __slots__ разрешите использовать только строго определенные
# локальные свойства в экземплярах класса).
# 2. Объявите класс Rectangle, хранящий координаты верхней левой и правой нижней точек. Создайте дескрипторы для
# записи и считывания этих значений в классе (атрибуты с данными координат должны быть приватными).
class Calendar:
    __slots__ = ["__day", "__month", "__year"]

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def __CheckValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def setDate(self, day, month, year):
        if Calendar.__CheckValue(day) and Calendar.__CheckValue(month) and Calendar.__CheckValue(year):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            raise AttributeError("Date must be number")

    def getDate(self):
        return self.__day, self.__month, self.__year


# d1 = Calendar(6, 5, 2003)
# print(d1.getDate())
# d1.setDate(2, 12, 2002)
# print(d1.getDate())

class CoordValue:
    def __set_name__(self, owner, name):  # Задаёт имя автоматически, без функции инит
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Rectangle:
    coordLeft = CoordValue()
    coordRight = CoordValue()
    coordTop = CoordValue()

    def __init__(self, top = 0, left=0, right=0):
        self.coordTop = top
        self.coordLeft = left
        self.coordRight = right


rect1 = Rectangle(1,3,5)
print(rect1.coordTop, rect1.coordLeft, rect1.coordRight)
