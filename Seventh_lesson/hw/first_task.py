import random


array = [ i for i in range(-100, 1000)]
random.shuffle(array)
print(array)


def bubble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]

    for i in range(len(array) // 2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1], array[i]

bubble(array)
print(array)