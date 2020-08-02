# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.
year_input = int(input())
if year_input % 400 == 0:
    print("Високосный")
elif year_input % 4 == 0 and year_input % 100 != 0:
    print("Високосный")
else:
    print("Обычный")
