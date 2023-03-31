def division(a, b):
    """
    Функция деления

    :param a: Первое число
    :type a: int
    :param b: Второе число
    :type b: int
    :return: Результат деления
    :rtype: float
    """
    return a / b


def division100():
    """
    Функция проверки деления 100 на число
    """
    try:
        x = int(input("Введите число: "))
    except ValueError:
        print("Введено не число")
        division100()
        return
    try:
        division(x, x)
    except ZeroDivisionError:
        print("Нельзя делить на 0")
        division100()
        return
    if x % 100 == 0:
        print("Делится")
    else:
        print("Не делится")


if __name__ == '__main__':
    division100()
