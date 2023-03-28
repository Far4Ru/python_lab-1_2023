from random import random


def task4():
    input()
    mv5 = ("Иванов", "Панин", "Юрина", "Королёва", "Шелькова", "Бекренева")
    mv4 = ("Весёлова", "Горбачева", "Прохоренкова", "Коллар", "Столетова", "Шевцова")
    mv_sport = tuple(random.sample(mv5, 6)[:3]+random.sample(mv4, 6)[:3])
    print(mv5)
    print(mv4)
    print(*mv_sport)
    print("Кол - во студентов", len(mv_sport))
    mv_sport = tuple(sorted(list(mv_sport)))
    print(*mv_sport)
    if "Иванов" in mv_sport:
        print(list(mv_sport).count("Иванов"), " - Иванов присутствует! ")
    else:
        print("Иванов, опять прогуливает!")


if __name__ == '__main__':
    task4()
