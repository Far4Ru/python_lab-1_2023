def division100():
    try:
        x = int(input("Введите число: "))
    except ValueError:
        print("Введите число!")
        division100()
        return
    try:
        x/x
    except ZeroDivisionError:
        print("Число не делится!")
        division100()
        return
    if x % 100 == 0:
        print("Делится")
    else:
        print("Не делится")


if __name__ == '__main__':
    division100()
