# n = int(input())
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

print(sieve(20))