from random import randint


def random_sum_expression():
    """
    Функция проверки результата случайной суммы чисел со счетчиком неверных ответов
    """
    wrong_answers = 0
    correct_answers = 0
    while True:
        a = randint(1, 10)
        b = randint(1, 10)
        c = int(input(f'{a} + {b} = '))
        if c == a + b:
            correct_answers += 1
            print('Правильно!')
        elif c != a + b:
            wrong_answers += 1
            print('Ответ неверный')
            if wrong_answers >= 3:
                print("Игра окончена. Правильных ответов:", correct_answers)
                break


if __name__ == '__main__':
    random_sum_expression()
