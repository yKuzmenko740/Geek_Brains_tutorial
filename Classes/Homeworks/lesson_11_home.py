class Table:
    def __init__(self, height: int, shape, material="wood"):
        self._material = material
        self._shape = shape
        self._height = height


class RectTable(Table):
    def __init__(self, *args, width: int, length: int):
        super().__init__(*args)
        self._length = length
        self._width = width
        self._shape = "Rect"

    def getArea(self):
        print(f"Площадь стола: {self._width * self._length}")
        print(self._shape)


class RoundTable(Table):
    def __init__(self, *args, radius: int):
        super().__init__(*args)
        self._radius = radius
        self._shape = "Round"

    def getArea(self):
        print(f"Площадь стола: {(self._radius ** 2) * 3, 14}")


# rect = RectTable(12, "Круглый", width=10, length=5)
# rect.getArea()

class Animal:
    def __init__(self, weigh:int, height:int, color:str):
        self._color = color
        self._height = height
        self._weigh = weigh

    def say(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод say()")


class Dog(Animal):
    def say(self):
        print(f"Dog is saying WOOF!WOOF!WOOF!")

class Fox(Animal):
    def say(self):
        print(f"Fox is saying FYR!FYR!FYR!")

class Cat(Animal):
    def say(self):
        print(f"Cat is saying MEOW!MEOW!MEOW!")

class Cow(Animal):
    def say(self):
        print(f"Dog is saying MOO!MOO!MOO!")


animals = []
animals.append(Dog(10,50,"black"))
animals.append(Fox(7,40,"orange"))
animals.append(Cat(7,30,"white"))
animals.append(Cow(100,150,"brown"))

for a in animals:
    a.say()
