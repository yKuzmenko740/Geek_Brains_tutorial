
#  методы класса, параметр self, конструктор и деструктор

class Point:
    def __init__(self,x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print('Deleting :' + self.__str__() )

    x = 1
    y = 1

    def setCoords(self, x, y):
        self.y = y
        self.x = x

# pt1 =Point()
# pt2 = Point(5)
# pt3 = Point(5, 10)
# print(pt1.__dict__)
# print(pt2.__dict__)
# print(pt3.__dict__)

pt = Point()
pt = 0
