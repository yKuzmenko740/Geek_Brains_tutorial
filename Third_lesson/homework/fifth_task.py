# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
SIZE = 10
nums = [random.randint(-100, 100) for i in range(SIZE)]
print(nums)

def negatives(array):
    neg = []
    for i in array:
        if i < 0:
            neg.append(i)
    m = neg[0]
    for i in neg:
        if i > m:
            m = i
        else:
            continue
    return f"Максимальное отрицательное число {m}, в позиции {array.index(m)}"

print(negatives(nums))

