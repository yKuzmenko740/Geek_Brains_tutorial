# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

import cProfile


def sieve(num):
    a = []
    for i in range(num * 10):
        a.append(i)

    a[1] = 0

    i = 2
    while i <= a[-1]:
        if a[i] != 0:
            j = i + i
            while j <= a[-1]:
                a[j] = 0
                j = j + i
        i += 1
    a = sorted(list(set(a)))
    a.remove(0)

    return a[num - 1]


# "task_2.sieve(5)"
# 1000 loops, best of 5: 19.4 usec per loop

# "task_2.sieve(15)"
# 1000 loops, best of 5: 111 usec per loop

#  "task_2.sieve(25)"
# 1000 loops, best of 5: 75.3 usec per loop

# "task_2.sieve(100)"
# 1000 loops, best of 5: 352 usec per loop

# "task_2.sieve(500)"
# 1000 loops, best of 5: 5.41 msec per loop

# cProfile.run("sieve(100)")
# 1 0.000 0.000 0.001 0.001 task_2.py: 3(sieve)




def prime(num):
    lst = []
    for i in range(2, num * 10):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[num-1]

# "task_2.prime(5)"
# 1000 loops, best of 5: 17.7 usec per loop

# "task_2.prime(15)"
# 1000 loops, best of 5: 99.6 usec per loop

# "task_2.prime(25)"
# 1000 loops, best of 5: 159 usec per loop

# "task_2.prime(100)"
# 1000 loops, best of 5: 1.47 msec per loop

# "task_2.prime(500)"
# 1000 loops, best of 5: 24.7 msec per loop

# cProfile.run("prime(100)")
#         1    0.004    0.004    0.004    0.004 task_2.py:46(prime)