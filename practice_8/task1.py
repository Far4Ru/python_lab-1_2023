from PIL import Image


def crop_image(filename, x1, y1, x2, y2):
    """
    Вырезает область из изображения и сохраняет в текущую папку под новым именем.
    """
    with Image.open("images/" + filename) as image:
        image.load()

    cropped_image = image.crop((x1, y1, x2, y2))
    # cropped_image.show()
    cropped_image.save("cropped_" + filename)


if __name__ == '__main__':
    crop_image("task1.jpg", 219, 79, 297, 134)
