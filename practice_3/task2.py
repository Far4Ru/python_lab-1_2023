def rare_words():
    """
    Функция проверки и вывода редкости слов
    """
    while True:
        word = input("Введите слово: ").lower()
        if word == 'stop':
            break
        if 'ф' in word:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")


if __name__ == '__main__':
    rare_words()
