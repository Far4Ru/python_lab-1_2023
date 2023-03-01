import re
import random
from collections import UserDict


class SynonymsDict(UserDict):
    def __setitem__(self, key, value):
        key = key.title()
        super().__setitem__(key, value)


def search_word(word):
    """
    Функция поиска синонимов в файле и вывода слова
    :param word: Искомое слово
    :type word: str
    :return: Истинность нахождения
    :rtype: bool
    """
    # Открыть файл
    with open('synonyms.txt') as f:

        # Найти строку с совпадением и синонимами по регулярному выражению
        result = re.search(rf'{word.title()} - [\w|; ]*', f.read())

        f.close()

        # Проверить нахождение
        if result is None:
            print("Не удалось найти синоним")
            return False

        # Отделить слово от синонимов
        synonyms = re.split(" - ", result.group(0))

        # Разделить синонимы в массив
        synonym_array = re.split("; ", synonyms[1])

        # Вывести случайное слово
        print(synonym_array[random.randint(0, len(synonym_array) - 1)])
        return True


if __name__ == '__main__':
    if search_word(input("Введите слово\n")) and input("Устривает ли подбор синонима? (да/нет): ").lower() == 'нет':
        # Запросить у пользователя подходит ли число
        # если нет, то запросить слово
        input("Ваш вариант синонима: ")

        # TODO: - внести слово в словарь
