import re
import random
from collections import UserDict


class SynonymsDict(UserDict):
    def __init__(self, mapping=None, /, **kwargs):
        if mapping is not None:
            mapping = {
                str(key).title(): value for key, value in mapping.items()
            }
        else:
            mapping = {}
        if kwargs:
            mapping.update(
                {str(key).title(): value for key, value in kwargs.items()}
            )
        super().__init__(mapping)

    def __setitem__(self, key, value):
        key = key.title()
        super().__setitem__(key, value)

    def random_value(self, key=None):
        if key is None:
            key = self.get_key()
        return self[key][random.randint(0, len(self) - 1)]

    def get_key(self):
        return list(self.data.keys()).pop()


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
            return {}

        # Отделить слово от синонимов
        synonyms = re.split(" - ", result.group(0))

        # Разделить синонимы в массив
        synonym_array = re.split("; ", synonyms[1])

        synonym_dict = SynonymsDict({synonyms[0]: synonym_array})

        # Вывести случайное слово
        print(synonym_dict.random_value())
        return synonym_dict


def paste_word(synonym_dict, word):
    """
    Функция вставки синонима в файл
    :param synonym_dict: Словарь с синонимами
    :type synonym_dict: SynonymsDict
    :param word: Новый синоним
    """
    if word in synonym_dict[synonym_dict.get_key()]:
        print("Синоним уже существует")
        return
    with open('synonyms.txt', "r") as f:
        filedata = f.read()
        synonym_stroke = f'{synonym_dict.get_key()} - {"; ".join(synonym_dict[synonym_dict.get_key()])}'
        filedata = filedata.replace(synonym_stroke, synonym_stroke + "; " + word)
        with open('synonyms.txt', 'w') as f:
            f.write(filedata)


if __name__ == '__main__':
    synonym_dict = search_word(input("Введите слово\n"))
    if synonym_dict != {} and input("Устривает ли подбор синонима? (да/нет): ").lower() == 'нет':
        # Запросить у пользователя подходит ли число
        # если нет, то запросить слово
        paste_word(synonym_dict, input("Ваш вариант синонима: "))
