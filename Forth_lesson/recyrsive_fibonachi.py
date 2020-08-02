import cProfile
import functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} Ok')


@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# cProfile.run("fib(15)")
# 1973/1    0.001    0.000    0.001    0.001 recyrsive_fibonachi.py:8(fib)

# cProfile.run("fib(20)")
# 21894 function calls (4 primitive calls) in 0.010 seconds

# "recyrsive_fibonachi.fib(10)"
# 1000 loops, best of 5: 64.1 usec per loop

# "recyrsive_fibonachi.fib(15)"
# 1000 loops, best of 5: 450 usec per loop

#  "recyrsive_fibonachi.fib(20)"
# 1000 loops, best of 5: 5.49 msec per loop
