from collections import Counter

a = Counter()
b = Counter('ababfabfsdafja')
c = Counter({"red": 2, "blue": 4})
d = Counter(cats=4, dogs=3)

print(a,b,c,d, sep="\n")

print(b["z"])
b["z"] = 0
print(b)

print(list(b.elements()))
print(b.most_common(1))

g = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)
g.subtract(f)
print(g)
print("*" * 50)

print(set(g))
print(dict(g))
g.clear()
print(g)

print("*" * 50)

x = Counter(a=3, b=1)
y = Counter(a=1, b=2)
print(x + y)
print(x - y)
print(x & y)
print(x | y)

print("*" * 50)

z = Counter(a=3, b=-1)
print(+z)
print(-z)

#sum(c.values()) - общее количество.
# c.clear() - очистить счётчик.
# list(c) - список уникальных элементов.
# set(c) - преобразовать в множество.
# dict(c) - преобразовать в словарь.
# c.most_common()[:-n:-1] - n наименее часто встречающихся элементов.
# c += Counter() - удалить элементы, встречающиеся менее одного раза.