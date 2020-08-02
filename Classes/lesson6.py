
# Метод init

class Cat:
    breed = 'pars'

    def set_value(self ,value ,age=0):
        self.name = value
        self.age = age

    def __init__(self ,name ,breed ,age ,color):
        print('Hello,object is : ', self, name, breed ,age ,color)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
