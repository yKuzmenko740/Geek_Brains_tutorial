import sys
import ctypes
import struct

a = 59
x = y = a
b = 125.54
c = "Hello world!"

print(id(a))  # адресс объекта в памяти
print(sys.getsizeof(a))

print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack("LLLLLLl", ctypes.string_at(id(a), sys.getsizeof(a))))
# первое число - счетчик ссылок, третье - указатель на тип объекта, последнее - значение объекта
print(id(int))

print("*" * 50)
print(id(b))  # адресс объекта в памяти
print(sys.getsizeof(b))

print(ctypes.string_at(id(b), sys.getsizeof(b)))
print(struct.unpack("LLLd", ctypes.string_at(id(b), sys.getsizeof(b))))
print(id(float))

print("*" * 50)
print(id(c))  # адресс объекта в памяти
print(sys.getsizeof(c))

print(ctypes.string_at(id(c), sys.getsizeof(c)))
print(struct.unpack("LLLLLLLLLLli" + "c" * 13, ctypes.string_at(id(c), sys.getsizeof(c))))

print("*" * 50)
lst = [1, 2, 3, 4]
print(struct.unpack("LLLL" + "L" * 5 * 4, ctypes.string_at(id(lst), sys.getsizeof(lst))))
