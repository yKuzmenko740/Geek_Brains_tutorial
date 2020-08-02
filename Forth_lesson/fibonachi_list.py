import cProfile


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} Ok')


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_dict(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_l[n]

    return _fib_dict(n)


# test_fib(fib_list)

#  "fibonachi_list.fib_list(10)"
# 1000 loops, best of 5: 15.8 usec per loop

# "fibonachi_list.fib_list(20)"
# 1000 loops, best of 5: 29.4 usec per loop

# "fibonachi_list.fib_list(100)"
# 1000 loops, best of 5: 93.9 usec per loop

# "fibonachi_list.fib_list(200)"
# 1000 loops, best of 5: 202 usec per loop

# fibonachi_list.fib_list(500)"
# 1000 loops, best of 5: 577 usec per loop

cProfile.run("fib_list(500)")
#      19/1    0.000    0.000    0.000    0.000 fibonachi_list.py:15(_fib_dict)
#     39/1    0.000    0.000    0.000    0.000 fibonachi_list.py:15(_fib_dict)
#  199/1    0.000    0.000    0.000    0.000 fibonachi_list.py:15(_fib_dict)
#     399/1    0.000    0.000    0.000    0.000 fibonachi_list.py:15(_fib_dict)
#     999/1    0.002    0.000    0.002    0.002 fibonachi_list.py:15(_fib_dict)