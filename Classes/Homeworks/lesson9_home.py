# 1. Объявите класс Rectangle (прямоугольник), в котором имеется статический метод, вычисляющий площадь
# прямоугольника. Этот метод принимает два параметра (ширину и длину), вызывается в конструкторе для вычисления
# площади конкретного прямоугольника и результат присваивается локальному свойству создаваемого экземпляра класса.
#
# 2. Создайте класс Dog (собака), в каждом его экземпляре создавайте несколько локальных свойств (например: имя,
# возраст, порода) и сделайте так, чтобы можно было создавать не более пяти экземпляров этого класса.

class Rectangle:

    def __init__(self, width, long):
        self.width = width
        self.long = long
        __area = 0

    @staticmethod
    def getArea(width, long):
        return long * width

    def returnArea(self):
        Rectangle.__area = self.width * self.long
        return Rectangle.__area


# rect = Rectangle(10,5)
#
# print(rect.getArea(10,5))
# print(rect.returnArea())


class Dog:
    __count_instance = 0

    def __new__(cls, *args, **kwargs):
        if cls.__count_instance != 5:
            cls.instance = super().__new__(cls)
            cls.__count_instance += 1
            return cls.instance
        else:
            print("Экземпляр уже существует ")

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

dog = Dog("Jack", 3, "Husky")
dog2 = Dog("Jack", 3, "Husky")
dog3 = Dog("Jack", 3, "Husky")
dog4 = Dog("Jack", 3, "Husky")
dog5 = Dog("Jack", 3, "Husky")



