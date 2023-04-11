from datetime import datetime


def magic_date_check(date_str):
    """
    Функция проверки магической даты

    :param date_str: Заданная дата
    :type date_str: str
    :return: Результат проверки
    :rtype: str
    """
    date = datetime.strptime(date_str, "%d.%m.%Y")
    if str(date.day * date.month) == str(date.year)[2:]:
        return "Магическая дата"
    else:
        return "Не магическая дата"


if __name__ == '__main__':
    print(magic_date_check(input("Введите дату: ")))
