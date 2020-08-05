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


c1 = Clock(8000)
c2 = Clock(200)
c3 = c1 + c2 + c2  # оператор сложения не работает с классом Clock(после перегрузки метода __add__ работает)
c1 += c2  # оператор  не работает с классом Clock(после перегрузки метода __iadd__ работает)
print(c1.getFormatTime())
