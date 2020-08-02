import random

size = 5
matrix = [[random.randint(1,10) for _ in range(size)] for _ in range(size)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()


# first_task
# sum_column = [0] * len(matrix[0])
# print(sum_column)
#
# for line in matrix:
#     sum_line = 0
#
#     for i,item in enumerate(line):
#         sum_line += item
#         sum_column[i] += item
#         print(f'{item:>5}', end='')
#     print(f"     | {sum_line}")
#
# print('-' * (len(matrix) * 5) )
#
# for s in sum_column:
#     print(f"{s:>5}", end="")

# second_task
for i in range(size):
    for j in range(size):
        if i == j:
            spam = matrix[i][j]
            matrix[i][j] = matrix[i][size -1 - j]
            matrix[i][size - 1 - j] = spam
print("*" * 30)
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()