class Point3D:
    def __init__(self, x=0, y=0,z=0):
        self.x = x
        self.y = y
        self.z = z


    def change_coord(self):
        self.x = int(input('Введите координату х'))
        self.y = int(input('Введите координату х'))
        self.z = int(input('Введите координату х'))
        print('Координаты изменены')

    def get_coord(self):
        b = (self.x, self.y, self.z)
        return b

pt = Point3D()
print(pt.get_coord())

class Point:
    def __init__(self, x=0, y=0,):
        self.x = x
        self.y = y

p1 = Point()
print(p1.__dict__)