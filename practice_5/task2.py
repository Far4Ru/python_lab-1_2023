from random import randint


def check_number_repeat():
    """
    Функция определения, есть ли в созданном списке повторяющиеся элементы
    """
    numbers = []
    for i in range(5):
        numbers.append(randint(0, 100))
    print(numbers)
    duplicate_numbers = {str(number) for number in numbers if numbers.count(number) > 1}
    print("Нет повторяющихся элементов") if len(duplicate_numbers) < 1 else print("Повторяется ", " ".join(duplicate_numbers))


if __name__ == '__main__':
    check_number_repeat()
