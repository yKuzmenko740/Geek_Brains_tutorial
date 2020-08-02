# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

a = [int(i) for i in input().split()]
max = [0, 0]
min = [0, 0]
summ = 0
for i, item in enumerate(a):
    if item > max[1]:
        max[1] = item
        max[0] = i
    else:
        continue
for i, item in enumerate(a):
    if item < min[1]:
        min[1] = item
        min[0] = i
    else:
        continue
if max[0] < min[0]:
    for i in range(max[0] , min[0]):
        summ += a[i]
    print(f"Сумма элементов : {summ- a[max[0]]}")
elif max [0] > min[0]:
    for i in range(min[0] , max[0]):
        summ += a[i]
    print(f"Сумма элементов :{summ - a[min[0]]}")
else:
    print("Между элементами нет чисел")
