def compare_passwords(fp, sp):
    """
    Функция сравнения паролей

    :param fp: Первый пароль
    :type fp: str
    :param sp: Второй пароль
    :type fp: str
    :return: Истинность совпадения паролей
    :rtype: bool
    """
    return fp == sp


def compare_passwords_result(fp, sp):
    """
    Функция вывода результата сравнения паролей

    :param fp: Первый пароль
    :type fp: str
    :param sp: Второй пароль
    :type fp: str
    :return: Строка с результатом сравнения паролей
    :rtype: str
    """
    if compare_passwords(fp, sp):
        return "Пароль принят"
    else:
        return "Пароль не принят"


if __name__ == '__main__':
    print(compare_passwords_result(input("Введите пароль\n"), input("Введите пароль повторно\n")))
