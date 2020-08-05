class AMD:
    def __init__(self):
        super().__init__()

    def showInfo(self):
        return "AMD"


class Intell:
    def __init__(self):
        super().__init__()

    def showInfo(self):
        return "Intell"


class NVidia:
    def __init__(self):
        super().__init__()

    def showInfo(self):
        return "NVidia"


class GeForce:
    def __init__(self):
        super().__init__()

    def showInfo(self):
        return "AMD"


class CPU(AMD, Intell):
    def __init__(self):
        super().__init__()

    def showInfo(self):
        return "CPU", super().showInfo()


class GPU(NVidia, GeForce):
    def __init__(self):
        super().__init__()

    def showInfo(self):
        return "GPU", super().showInfo()


class Memory:
    def __init__(self):
        super().__init__()

    def showInfo(self):
        return "Memory"


class Motherboard(CPU, GPU, Memory):
    def __init__(self, param1, param2):
        self._param2 = param2
        self._param1 = param1
        super().__init__()

    def showInfo(self):
        return "Motherboard", super().showInfo(), self._param1, self._param2


m = Motherboard(12,12)
print()
