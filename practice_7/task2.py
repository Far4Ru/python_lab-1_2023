import PIL
from PIL import Image


def get_small_copy(filename):
    """
    Сохраняет уменьшенную в три раза копию изображения
    Сохраняет горизонтальный и вертикальный зеркальный образ изображения
    Сохранения идут в текущую папку под новым именем.
    """
    with Image.open(filename) as image:
        image.load()

    # уменьшенная в три раза копия изображения
    small_image = image.resize((image.width // 3, image.height // 3))
    small_image.save("new_image.jpg")

    # горизонтальный зеркальный образ изображения
    new_img = small_image.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    new_img.save("new_image_1.jpg")

    # вертикальный зеркальный образ изображения
    new_img = small_image.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    new_img.save("new_image_2.jpg")


if __name__ == '__main__':
    get_small_copy("images/task2.jpg")
