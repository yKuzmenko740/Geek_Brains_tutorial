# режимы доступа - public, private, protected. Геттеры и сеттеры
class Point:

    WIDTH = 5
    __slots__ = ['__x', '__y']

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print('Coords must be numbers')

    def getCoords(self):
        return self.__x, self.__y

    def __getattribute__(self, item):
        if item == '_Point__x':
            return 'Private value'
        else:
            return object.__getattribute__(self,item)

    def __setattr__(self, key, value):
        if key == 'WIDTH':
            raise AttributeError
        else:
            # чтобы небыло рекурсии
            self.__dict__[key] = value

    def __getattr__(self, item):
        print('__getattr__ ' + item)

    def __delattr__(self, item):
        print('__delattr__ ' + item)

pt = Point(1, 2)
pt.setCoords(10, 20)
print(pt.getCoords())
print(pt._Point__x)
# pt.WIDTH = 5
pt.z =1
del pt.z