# перегрузка операторов: __add__, __iadd__, __getitem__, __setitem__ и другие

class Clock:
    __DAY = 86400  # число секунд в дне

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("Секунды должны быть целым числом")

        self.__secs = secs % self.__DAY  # гарантия того что локальное свойство не будет привышать значения __DAY

    def getFormatTime(self):
        s = self.__secs % 60  # секунды
        m = (self.__secs // 60) % 60  # минуты
        h = (self.__secs // 3600) % 24  # часы
        return f"{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}"

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")

        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")

        self.__secs += other.getSeconds()
        return self

    def getSeconds(self):
        return self.__secs

    def __nq__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        return self.__secs == other.getSeconds()

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == "hour":
            return (self.__secs // 3600) % 24
        elif item == "min":
            return (self.__secs // 60) % 60
        elif item == "sec":
            return self.__secs % 60

        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")

        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")

        s = self.__secs % 60  # секунды
        m = (self.__secs // 60) % 60  # минуты
        h = (self.__secs // 3600) % 24  # часы

        if key == "hour":
            self.__secs = s + 60*m + value * 3600
        elif key == "min":
            self.__secs = s + 60*value + h*3600
        elif key == "sec":
            self.__secs = value + 60*m + h*3600






c1 = Clock(200)
c2 = Clock(200)
c3 = c1 + c2 + c2  # оператор сложения не работает с классом Clock(после перегрузки метода __add__ работает)
# c1 += c2
# c2 += c1  # оператор  не работает с классом Clock(после перегрузки метода __iadd__ работает)
print(c1.getFormatTime())
c1['hour'] = 10
print(c1['hour'])  # с помощью перегрузки метода __getitem__
print(c1.getFormatTime())
if c1 == c2:
    print("Времена равны")
