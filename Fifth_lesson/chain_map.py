from collections import ChainMap

# цепочка из словарей, позволяет организовать роботу с несколькими словарями

d_1 = {'a': 2, "b": 4, 'c': 6}
d_2 = {'a': 10, "b": 7, 'd': 40}

d_map = ChainMap(d_1, d_2)
print(d_map)
d_2['a'] = 100  # ссылочная структура данных
print(d_map)

print(d_map['a'])
print(d_map['d'])

print("*" * 100)

# Methods

x = d_map.new_child({"a": 12, "b": 32, 'd': 333})  # ADD NEW DICT AT THE BEGINNING OF THE COLLECTION
print(x)

# getting dictionaries in the collection
print(x.maps[0])
print(x.maps[-1])

# getting dicts before method new_child()
print(x.parents)

print("*" * 100)

y = d_map.new_child()
print(y)
print(y['a'])
y["a"] = 1 # если нет ключа "а" в первом словаре,то оно добавляется
print(y)

print(list(y)) # ключи по алфавитному порядку
print(list(y.values()))  # значение

