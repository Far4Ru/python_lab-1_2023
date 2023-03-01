COLORS = ['красный', 'синий', 'желтый']
MIX_COLORS = ['фиолетовый', 'оранжевый', 'зеленый']


def mix_colors(fc, sc):
    """
    Функция вывода цвета, полученного в результате смешения двух цветов

    :param fc: Первый цвет
    :type fc: str
    :param sc: Второй цвет
    :type fc: str
    :return: Полученный цвет
    :rtype: str
    :raises ValueError: Неверный цвет
    """
    fc = fc.lower()
    sc = sc.lower()
    if fc not in COLORS or sc not in COLORS:
        raise ValueError('Введен неверный цвет')
    else:
        if (fc == COLORS[0] and sc == COLORS[1]) or (sc == COLORS[0] and fc == COLORS[1]):
            # Смешивание красного и синего
            return MIX_COLORS[0]
        elif (fc == COLORS[0] and sc == COLORS[2]) or (sc == COLORS[0] and fc == COLORS[2]):
            # Смешивание красного и желтого
            return MIX_COLORS[1]
        elif (fc == COLORS[1] and sc == COLORS[2]) or (sc == COLORS[1] and fc == COLORS[2]):
            # Смешивание синего и желтого
            return MIX_COLORS[2]
    # Смешивание одинаковых цветов
    return fc


if __name__ == '__main__':
    print(mix_colors(input("Первый цвет\n"), input("Второй цвет\n")))
