from PIL import Image


def get_holidays():
    """
    Возвращает словарь, содержащий перечень пары «Название праздника – имя_файла с открыткой к нему».
    """
    return {"Новый год": "task2_1.png",
            "23 февраля": "task2_2.png",
            "8 марта": "task2_3.jpg",
            "День рождения": "task2_4.jpg"}


def get_postcard(holiday, holidays):
    """
    Вывод нужной открытки на экран.
    """

    filename = holidays[holiday]
    with Image.open("images/" + filename) as image:
        image.load()

    image.show()


if __name__ == '__main__':
    holiday_list = "Новый год\n" +\
                   "23 февраля\n" +\
                   "8 марта\n" +\
                   "День рождения\n"
    get_postcard(input("К какому празднику нужна открытка?\n" + holiday_list), get_holidays())
