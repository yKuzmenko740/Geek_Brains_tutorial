class Point3D:
    def __init__(self, x: int, y: int, z: int):
        self.__x = x
        self.__y = y
        self.__z = z

    def getCoords(self):
        return self.__x, self.__y, self.__z

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item.upper() == "X":
            return self.__x
        elif item.upper() == 'Y':
            return self.__y
        elif item.upper() == 'Z':
            return self.__z

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")

        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")

        if key.upper() == "X":
            self.__x = value
        elif key.upper() == "Z":
            self.__z = value
        elif key.upper() == "Y":
            self.__y = value
    def __add__(self, other):
        return Point3D((self.__x + other.getX()), (self.__y + other.getY()), (self.__z + other.getZ()))

    def __sub__(self, other):
        return Point3D((self.__x - other.getX()), (self.__y - other.getY()), (self.__z - other.getZ()))

    def __mul__(self, other):
        return Point3D((self.__x * other.getX()), (self.__y * other.getY()), (self.__z * other.getZ()))

    def __truediv__(self, other):
        return Point3D((self.__x / other.getX()), (self.__y / other.getY()), (self.__z / other.getZ()))

    def __eq__(self, other):
        if self.__x == other.getX() and self.__y == other.getY() and self.__z == other.getZ():
            return True
        return False

    def ___nq__(self, other):
        return not self.__eq__(other)


c1 = Point3D(1, 2, 3)
c2 = Point3D(2, 2, 3)
print(c1.getCoords())
c1['z'] = 10
print(c1["z"])
print(c1.getCoords())
