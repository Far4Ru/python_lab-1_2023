from random import sample


def init_groups():
    """
    Создается два списка: один из 10 фамилий студентов одной группы, другой из 10 фамилий студентов другой группы.
    """
    mv5 = ("Иванов", "Стиценко", "Юрина", "Бекренёва", "Королёва", "Шелькова", "Семёнов", "Рословец", "Пузанов", "Панин")
    mv4 = ("Веселова", "Соколов", "Прохоренкова", "Коллар", "Белоцерковский", "Шевцова", "Николаева", "Родионова", "Крупницкий")
    # print(group1)
    # print(group2)
    return {"mv5": mv5, "mv4": mv4}


def make_sport_group(group1, group2):
    """
    Создается спортивная команда (один кортеж) по 5 любых студентов из каждой группы.
    """
    # sample() - случайная выборка нескольких элементов последовательности без замены.
    group = tuple(sample(group1, len(group1))[:5] + sample(group2, len(group2))[:5])
    # print(*group)
    return group


def sport_group_len(group):
    """
     Выводится длина кортежа спортивной команды.
    """
    print("Студентов", len(group))


def sport_sort(group):
    """
    Сортируется кортеж по алфавиту.
    """
    sorted_group = tuple(sorted(list(group)))
    # print(*group)
    return sorted_group


def sport_search(name, group):
    """
    Определяется, входит ли в полученную команду студент "Иванов". И сколько раз встречается эта фамилия в кортеже.
    """
    if name in group:
        print(list(group).count(name), name + " присутствует")
    else:
        print(name + " отсутствует")


if __name__ == '__main__':
    groups = init_groups()
    sport_group = make_sport_group(groups['mv5'], groups['mv4'])
    sport_group_len(sport_group)
    sorted_sport_group = sport_sort(sport_group)
    sport_search("Иванов", sorted_sport_group)
