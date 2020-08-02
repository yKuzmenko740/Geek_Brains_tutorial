# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
alphabet = list("abcdefghijklmnopqrstuvwxyz")
input = int(input("Введите номер буквы в алфавите: "))
print(f"Буква под номер {input}: {alphabet.__getitem__(input - 1)}")