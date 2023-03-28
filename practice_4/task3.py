from datetime import datetime


def task3():
    x = datetime.strptime(input("Введите дату: "), "%d.%m.%Y")
    if str(x.day * x.month) == str(x.year)[2:]:
        print("Магическая дата")
    else:
        print("Не магическая дата")


if __name__ == '__main__':
    task3()
