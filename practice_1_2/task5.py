def join_words(n):
    """
    Функция соединения введеных слов с заданным количеством

    :param n: Количество слов
    :type n: int
    :return: Строка, разделенная пробелами
    :rtype: str
    """
    stroke = ""
    for i in range(n):
        word = input("Введите слово: ")
        if i == 0:
            stroke += word
        else:
            stroke += " " + word
    return stroke


if __name__ == '__main__':
    print(join_words(int(input("Количество слов\n"))))
