lst = []
lst.append(1)
lst.extend([2, 3, 4])
print(lst)

lst.insert(1, 5)
print(lst)

last = lst.pop()
print(last,lst)

lst.remove(5)
print(lst)

















# How memory in list generated
# allocated = 0
# for newsize in range(1000):
#     if allocated <newsize:
#         new_allocated = (newsize >> 3) + (3 if newsize < 9 else 6)
#         allocated = newsize + new_allocated
#     print(newsize,allocated)
