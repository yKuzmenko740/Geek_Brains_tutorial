# Атрибуты экземпляры класса

class Car:
    model = "BMW"
    engine = 1.6

# import sys; print('Python %s on %s' % (sys.version, sys.platform))
# sys.path.extend(['C:\\Users\\User\\Desktop\\GB', 'C:/Users/User/Desktop/GB'])
# PyDev console: starting.
# Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
# class Car:
# ...     model = "BMW"
# ...     engine = 1.6
# ...
# a1 = Car()
# a2 = Car()
# Car.__dict__
# mappingproxy({'__module__': '__main__', 'model': 'BMW', 'engine': 1.6, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
# a2.engine
# 1.6
# a1.__dict__
# {}
# a2.__dict__
# {}
# a1.seat = 4
# a1.__dict__
# {'seat': 4}
# a1.model = "Mers"
# a1.__dict__
# {'seat': 4, 'model': 'Mers'}
# a1.model
# 'Mers'
# a2.size = 80
# a2.size
# 80
# Car.__dict__
# mappingproxy({'__module__': '__main__', 'model': 'BMW', 'engine': 1.6, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
# Car.r = 100
# a1.r
# 100
# del a1.model
