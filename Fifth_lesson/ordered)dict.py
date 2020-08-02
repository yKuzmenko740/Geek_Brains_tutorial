from collections import OrderedDict

a = {"cat": 5, "dog": 2, "mouse": 4}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)

b = {"cat": 5, "dog": 2, "mouse": 4}
new_b = OrderedDict(sorted(a.items(), key=lambda x: x[1])) # sorted by keys and items
print(new_b)

new_b.move_to_end("mouse")  # перенос в конец
new_b.move_to_end("mouse", last=False)  # перенос в начало
print(new_b)

new_b.popitem()  # удаляет последний элемент
print(new_b)

new_b.popitem(last=False)  # удаляет первый элемент
print(new_b)

new_b["dog"] = 8  # старое значение меняется,но порядок остается
print(new_b)

print("*" * 50)

new_c = OrderedDict(sorted(a.items(), key= lambda x: len(x[0]))) # sorted by key len
print(new_c)

# for key in reversed(new_c):
#     print(key, new_c[key])