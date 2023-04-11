def check_lucky_ticket():
    """
    Функция, проверяющая является ли номер счастливым
    """
    print("Введите номер билета: ")
    a = [int(i) for i in input()]
    if len(a) % 2 != 0:
        print("В билете должно быть четное количество цифр")
        check_lucky_ticket()
        return
    if sum(a[:int(len(a)/2)]) == sum(a[int(len(a)/2):]):
        print("Счастливый билет")
    else:
        print("Не счастливый билет")


if __name__ == '__main__':
    check_lucky_ticket()
