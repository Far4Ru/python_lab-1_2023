def get_cost(word):
    """
    Вычисление стоимости введенного слова.
    """
    letter_prices = {
        "авеинорст": 1,
        "дклмуп": 2,
        "бгёья": 3,
        "йы": 4,
        "жзхцч": 5,
        "шэю": 8,
        "фщъ": 10
    }
    cost = 0
    for letter in word:
        for letters, price in letter_prices.items():
            if letter.lower() in letters:
                cost += price
    print("Стоимость слова:", cost)


if __name__ == '__main__':
    get_cost(input("Введите слово: "))
