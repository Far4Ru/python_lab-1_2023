from PIL import Image


def add_watermark(filename):
    """
    Добавление на изображение водяной знак
    """
    watermark = "images/watermark.jpeg"
    with Image.open(watermark) as watermark_image:
        watermark_image.load()

    watermark_image = Image.open(watermark).convert("RGBA")
    watermark_image.putalpha(50)
    with Image.open("images/" + filename) as image:
        image.load()

    watermark_image = watermark_image.resize((image.width, image.height))
    image.paste(watermark_image, (image.width // 2 - watermark_image.width // 2, image.height // 2 - watermark_image.height // 2), watermark_image)
    image.save("watermarked_" + filename)


if __name__ == '__main__':
    add_watermark("task4.jpg")
