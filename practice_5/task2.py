
def task2():
    s = [11, 33, 77, 99, 99]
    duplicate = {str(x) for x in s if s.count(x) > 1}
    x = lambda: print("Нет повторяющихся элементов")
    y = lambda: print("Повторяется: ", " ".join(duplicate))
    x() if len(duplicate) < 1 else y()


if __name__ == '__main__':
    task2()
