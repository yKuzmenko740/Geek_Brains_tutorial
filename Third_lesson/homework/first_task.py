# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.
import cProfile

nums = [int(i) for i in range(2, 100)]


def crat(array):
    for x in range(2, 10):
        j = 0
        for i in array:
            if i % x == 0:
                j += 1
        print(f"{x} кратны {j} чисел")


cProfile.run("crat(nums)")
