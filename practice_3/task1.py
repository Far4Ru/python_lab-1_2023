def join_words():
    """
    Функция соединения введеных слов с заданным количеством
    Ввод слов останавливается словом 'stop'

    :return: Строка, разделенная пробелами
    :rtype: str
    """
    stroke = ""
    while True:
        word = input("Введите слово: ")
        if word == 'stop':
            break
        if stroke == "":
            stroke += word
        else:
            stroke += " " + word
    return stroke


if __name__ == '__main__':
    print(join_words())
