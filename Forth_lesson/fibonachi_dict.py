import cProfile
def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} Ok')

def fib_dict(n):
    fib_d = {0:0, 1: 1}
    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n-1) + _fib_dict(n-2)
        return fib_d[n]
    return _fib_dict(n)

# test_fib(fib_dict)

# "fibonachi_dict.fib_dict(10)"
# 1000 loops, best of 5: 7.98 usec per loop

#  "fibonachi_dict.fib_dict(15)"
# 1000 loops, best of 5: 11.4 usec per loop

#  "fibonachi_dict.fib_dict(20)"
# 1000 loops, best of 5: 15.5 usec per loop

#  "fibonachi_dict.fib_dict(25)"
# 1000 loops, best of 5: 21.2 usec per loop


cProfile.run("fib_dict(900)")



