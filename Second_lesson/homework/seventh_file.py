n = int(input("Введите число: "))
symma = 0
x = 0
for i in range(1, n + 1):
    x += 1
    symma += x
if symma == n*(n+1)/2:
    print("Равенство: 1+2+...+n = n(n+1)/2 -  выполняется. ")
else:
    print("Равенство: 1+2+...+n = n(n+1)/2 - не выполняется.")