# Функция сравнения паролей
def compare_passwords(fp, sp):
    return fp == sp


# Тестирование функции
input_fp = input("Введите пароль\n")
input_sp = input("Введите пароль повторно\n")
if compare_passwords(input_fp, input_sp):
    print("Пароль принят")
else:
    print("Пароль не принят")