def is_leap_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False


def is_leap_year_result(year):
    if is_leap_year(year):
        return "Год " + str(year) + " - високосный"
    else:
        return "Этот год не високосный"


if __name__ == '__main__':
    print(is_leap_year_result(int(input("Введите год\n"))))
