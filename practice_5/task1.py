def task1():
    num = int(input("Введите число: "))
    x = [11, 33, 55, 77, 99]
    if num in x:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")


if __name__ == '__main__':
    task1()
