import re
import random
from collections import UserDict


class SynonymsDict(UserDict):
    def __setitem__(self, key, value):
         key = key.title()
         super().__setitem__(key, value)


def search_word(word):
    # Открыть файл
    f = open('synonyms.txt')

    # Найти строку с совпадением и синонимами по регулярному выражению
    # TODO: - составить выражение
    result = re.match(word, f.read())

    f.close()

    # TODO: - проверить нахождение

    # Отделить слово от синонимов
    synonyms = re.split(" - ", result)

    # Разделить синонимы в массив
    synonym_array = re.split(" ; ", synonyms[1])

    # Вывести случайное слово
    return synonym_array[random.randint(0, len(synonym_array))]


if __name__ == '__main__':
    print(search_word(input("Введите слово")))
    # TODO: - запросить у пользователя подходит ли число
    # TODO: - если нет, то запросить слово
    # input()
    # TODO: - внести слово в словарь

