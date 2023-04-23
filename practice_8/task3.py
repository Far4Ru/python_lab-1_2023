from PIL import Image, ImageDraw, ImageFont


def name_to_postcard(name, filename):
    """
    Добавление на заданную открытку текста «<имя>, поздравляю!»
    """

    with Image.open("images/" + filename) as image:
        image.load()

    # используется файл с жирными символами шрифта Arial
    font = ImageFont.truetype("fonts/arial_bold.ttf", 25)
    draw_text = ImageDraw.Draw(image)
    draw_text.text(
        (image.width // 2, image.height // 2 - 155),
        name + ", поздравляю!",
        font=font,
        fill='#FFFFFF'
    )
    image.show()
    image.save(name + "_postcard.png")


if __name__ == '__main__':
    name_to_postcard(input("Введите имя получателя: "), "task2_4.jpg")
