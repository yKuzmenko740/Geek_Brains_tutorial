# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8,
# 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

nums = [int(i) for i in input().split()]
ind = []

for i, item in enumerate(nums):
    if item % 2 == 0:
        ind.append(i)
print(f"Индексы чётных элементов в массиве {nums}: {ind}")
