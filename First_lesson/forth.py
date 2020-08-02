# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

alphabet = "abcdefghijklmnopqrstuvwxyz"
first_letter = input().lower()
second_letter = input().lower()
print(f"{first_letter.upper()} находится на {alphabet.find(first_letter) + 1} месте")
print(f"{second_letter.upper()} находится на {alphabet.find(second_letter) + 1} месте")
print(
    f"Между {first_letter} и {second_letter} находится {(alphabet.find(second_letter)) - (alphabet.find(first_letter))}")
