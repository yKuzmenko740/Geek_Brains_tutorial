def binary(num):
    s = ''
    while num > 0:
        s = f"{num % 2}{s}"
        num //= 2
    return s

# print(binary(255))

while True:
    n = int(input())
    if n!=0:
        print(binary(n))
    else:
        break