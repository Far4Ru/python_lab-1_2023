def seat_number_type(number):
    if number < 38:
        if number % 2 == 0:
            return "Купе, нижнее"
        else:
            return "Купе, верхнее"
    elif number <= 54:
        if number % 2 == 0:
            return "Боковое, нижнее"
        else:
            return "Боковое, верхнее"
    return "Место не найдено"


if __name__ == '__main__':
    print(seat_number_type(int(input("Введите номер места в вагоне\n"))))
