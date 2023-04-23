from random import randint


def guess(number):
    """
    Функция выводит исходный список из пяти чисел,
    число пользователя
    и соответствующие сообщение ("Поздравляю, Вы угадали число!" или "Нет такого числа!").
    """
    numbers = []
    for i in range(5):
        numbers.append(randint(0, 100))
    print(numbers)
    print(number)
    if number in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")


if __name__ == '__main__':
    guess(int(input("Введите число: ")))
