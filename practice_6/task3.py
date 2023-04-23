from random import randint


def get_students():
    """
    Функция, которая возвращает множество студентов, которые знают некоторое количество языков
    """
    students = ("Иванов", "Стиценко", "Юрина", "Бекренёва", "Королёва", "Шелькова", "Семёнов", "Рословец", "Пузанов", "Панин")
    students_languages = {}
    languages = ['Английский', 'Русский', 'Японский', 'Чилийский', 'Китайский']

    for surname in students:
        students_languages[surname] = []
        for language in languages:
            if randint(0, 100) < 10:
                students_languages[surname].append(language)
    return students_languages


def get_languages_known(students):
    """
    Функция определения количество различных языков, которые знают студенты.
    Выводит отсортированный список этих языков.
    """
    languages = []
    for surname in students:
        for language in students[surname]:
            if language not in languages:
                languages.append(language)
    sorted_languages = sorted(languages)
    print('Список различных языков:', *sorted_languages)


def get_chinese_students(language, students):
    """
    Вывод списока студентов, которые знают китайский язык.
    """
    chinese_students = []
    for surname in students:
        if language in students[surname]:
            chinese_students.append(surname)

    print("Студенты, знающие " + language + ":", *chinese_students)


if __name__ == '__main__':
    student_list = get_students()
    get_languages_known(student_list)
    get_chinese_students('Китайский', student_list)
