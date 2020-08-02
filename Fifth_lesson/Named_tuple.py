from collections import namedtuple

# Like dictionaries they contain keys that are hashed to a particular value. But on contrary, it supports both access
# from key value and iteration, the functionality that dictionaries lack.

hero_1 = ('Aaz', "izverg", 100, 0.0, 250)
print(hero_1[4])



class Person:
    def __init__(self, name, race, healtg, mana, strenght):
        self.name = name
        self.race = race
        self.healtg = healtg
        self.mana = mana
        self.strenght = strenght


hero_2 = Person('Aaz', "izverg", 100, 0.0, 250)


New_person = namedtuple("New_person", "name, race, healtg, mana, strenght")
hero_3 = New_person('Aaz', "izverg", 100, 0.0, 250)

print(hero_3[:])

prop = ["name", "3race", "healtg", "_mana", "strenght",]
New_person_1 = namedtuple("New_person", prop, rename=True) # rename=True -> rename unsupported names
hero_4 = New_person_1('Aaz', "izverg", 100, 0.0, 250)
print(hero_4)

print("*" * 50)

Point = namedtuple("Point", "x, y, z")

p1 = Point(2, z=3, y=4)
print(p1)

t = [5, 10, 15]
p2 =Point._make(t)
print(p2)

d2 = p2._asdict() # namedtuple into OrderedDict
print(d2)

p3 = p2._replace(x=6) # change value in tuple
print(p3)

print(p3._fields) # fields(first variables) in tuple

print("*" * 50)

New_Point = namedtuple("New_point", "x, y, z", defaults=[0,0]) # defaults -> значения по умолчанию
p4 = New_Point(5)
print(p4)

# print(p4._field_defaults)

# создание именованого кортежа на основе словаря
dct = {"x": 10, 'y':20, 'z': 30}
p5 = New_Point(**dct)
print(p5)
