def division3(x):
    if int(x) % 3 == 0:
        return "Делится"
    else:
        return "Не делится"


if __name__ == '__main__':
    print(division3(input("Введите число: ")))
