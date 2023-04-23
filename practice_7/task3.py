from os import path, mkdir
from PIL import Image, ImageFilter


def filter_images(filenames):
    """
    Примененение ко всем файлам фильтр
    Сохранение изображений в новую папку под новыми именами.
    """
    directory = "results"
    for filename in filenames:
        with Image.open("images/" + filename) as image:
            image.load()
            new_image = image.filter(ImageFilter.EMBOSS)
            # new_image.show()
            add_dir(directory)
            new_image.save(directory + "/emboss_" + filename)


def add_dir(name):
    """
    Добавление новой папки под новым именем.
    """
    if not path.exists(name):
        mkdir(name)


if __name__ == '__main__':
    filter_images(["1.png", "2.png", "3.png", "4.png", "5.png"])
