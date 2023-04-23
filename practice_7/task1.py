from PIL import Image


def open_image(filename):
    """
    Открытие и вывод файла на экран и вывод его информации в консоль.
    """
    with Image.open(filename) as image:
        image.load()
        get_image_info(image)
        image.show()


def get_image_info(image):
    """
    Вывод информации о размере изображения, его формате и его цветовой модели.
    """
    width, height = image.size
    image_format = image.format
    image_mode = image.mode
    print("Ширина:", width)
    print("Высота:", height)
    print("Формат:", image_format)
    print("Цветовая модель:", image_mode)


if __name__ == '__main__':
    open_image("images/task1.png")
