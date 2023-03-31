def division3(n):
    """
    Функция проверки делимости числа на 3

    :param n: Заданное число
    :type n: int
    :return: Строка о делимости числа на 3
    :rtype: str
    """
    return "Число делится на 3" if n % 3 == 0 else "Число не делится на 3"


if __name__ == '__main__':
    print(division3(int(input("Введите число: "))))
