seat_number = int(input("Введите номер места в вагоне\n"))
if seat_number < 38:
    if seat_number % 2 == 0:
        print("Купе, нижнее")
    else:
        print("Купе, верхнее")
elif seat_number <= 54:
    if seat_number % 2 == 0:
        print("Боковое, нижнее")
    else:
        print("Боковое, верхнее")
else:
    print("Место не найдено")