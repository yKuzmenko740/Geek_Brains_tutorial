# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = []
max = [0, 0]
min = [0, 0]
for i in range(20):
    a.append(int(random.random() * 30) - 10)
for i,item in enumerate(a):
    if item > max[1]:
        max[1] = item
        max[0] = i
    else:
        continue
for i,item in enumerate(a):
    if item < min[1]:
        min[1] = item
        min[0] = i
    else:
        continue
print(a)
print("Максимальное и минимальное значение в массиве: ", max, min)
a[min[0]] = max[1]
a[max[0]] = min[1]
print(a)

