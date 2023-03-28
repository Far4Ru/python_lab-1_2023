def task4():
    print("Введите номер билета: ")
    a = [int(i) for i in input()]
    if len(a) % 2 != 0:
        print("Введите четное кол-во чисел: ")
        task4()
        return
    if sum(a[:int(len(a)/2)]) == sum(a[int(len(a)/2):]):
        print("Счастливый билет!")
    else:
        print("Не является счастливым билетом:(")


if __name__ == '__main__':
    task4()
