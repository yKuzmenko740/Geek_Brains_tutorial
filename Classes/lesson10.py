# простое наследование классов, режим доступа protected

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):  # переопределяем стандартное сообщение класса
        return f"({self.__x}, {self.__y})"


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        # : это нотация(подсказка для разработчика)
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def getWidth(self):
        return self.__width


class Line(Prop):
    def __init__(self, *args):
        print("Переопределенный конструктор Line")
        super().__init__( *args) # Выхов конструктора базового класса(чтобы небыло ошибки)
        self.__width = 5 # переопределяем частную переменную _Prop__width в _Line__width
    def drawLine(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.__width}") # переменная __width будет
        # выведена как 5, т.к она была переопределена выше


class Rect(Prop):
    # DRY - DON'T REPEAT YOURSELF
    # def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
    #     # : это нотация(подсказка для разработчика)
    #     self._sp = sp
    #     self._ep = ep
    #     self._color = color
    #     self._width = width
    def drawRect(self):
        print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")


print(issubclass(Point, object))  # True если класс Point аследуется от класса object
l = Line(Point(1, 2), Point(10, 20))
l.drawLine()
# Рисование линии: <__main__.Point object at 0x0000019B0C43C0B8>, <__main__.Point object at 0x0000019B0C43C080>, red,
# 1 - это стандартное сообщение к ласса Point

r = Rect(Point(20, 30), Point(70, 80))
r.drawRect()
