# 4. Определить, какое число в массиве встречается чаще всего.
a = [int(i) for i in input().split()]
m = 0
z = 0
for i in a:
    if a.count(i) > m :
        m = a.count(i)
for x in a:
    if a.count(x) == m:
        z = x
print(f"{z} встречается больше всего раз ({m})")