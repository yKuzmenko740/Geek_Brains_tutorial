# 1. Создайте суперкласс «Персональные компьютеры» и на его основе подклассы: «Настольные ПК» и «Ноутбуки». В базовом
# классе определите общие свойства: размер памяти, диска, модель, CPU. А в производных классах уникальные свойства:
# для настольных: монитор, клавиатура, мышь, их габариты; и метод для вывода этой информации в консоль; для
# ноутбуков: габариты, диагональ экрана; и метод для вывода этой информации в консоль. 2. Повторите это задания для
# суперкласса «Человек» и подклассов «Мужчина» и «Женщина». Подумайте, какие общие характеристики можно выделить в
# суперкласс и какие частные свойства указать в подклассах.1. Создайте суперкласс «Персональные компьютеры» и на его
# основе подклассы: «Настольные ПК» и «Ноутбуки». В базовом классе определите общие свойства: размер памяти, диска,
# модель, CPU. А в производных классах уникальные свойства:
# для настольных: монитор, клавиатура, мышь, их габариты; и метод для вывода этой информации в консоль;
# для ноутбуков: габариты, диагональ экрана; и метод для вывода этой информации в консоль.

# 2. Повторите это задания для
# суперкласса «Человек» и подклассов «Мужчина» и «Женщина». Подумайте, какие общие характеристики можно выделить в
# суперкласс и какие частные свойства указать в подклассах.

class PC:
    def __init__(self, memory_size: int, disk_size: int, model: str, cpu: str):
        self._cpu = cpu
        self._model = model
        self._disk_size = disk_size
        self._memory_size = memory_size

    def __str__(self):
        return f"({self._memory_size}, {self._disk_size}, {self._model}, {self._cpu})"


class DesktopComp(PC):
    def __init__(self, *args, monitor: str, keyboard: str, mouse: str, profile: str):
        super().__init__(*args)
        self._profile = profile
        self._mouse = mouse
        self._keyboard = keyboard
        self._monitor = monitor

    def desktopInfo(self):
        print(f"""Настольный компьютер: {self._model} - CPU:{self._cpu}, Memory size: {self._memory_size},Disk size:{self._disk_size}. Монитор: {self._monitor}, Клавиатура: {self._keyboard}, Мышь:{self._mouse},Габариты {self._profile}""")


class Laptop(PC):
    def __init__(self, *args, profile: str, diag: int):
        super().__init__(*args)
        self._diag = diag
        self._profile = profile

    def laptopInfo(self):
        print(f"""Ноутбук: {self._model} - CPU:{self._cpu}, Memory size: {self._memory_size},Disk size: \
{self._disk_size}.Диагональ экрана: {self._diag}, Габариты: {self._profile}""")


lap = Laptop(12,100,"test","testing",profile="SQUARE", diag=100)
lap.laptopInfo()