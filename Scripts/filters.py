import os
from random import *
from PIL import Image

def grey_world(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))

            a = (r + g + b) // 3
            r = 0
            g = 0
            b = 0

            r, g, b = (a, a, a)

            img.putpixel((i, j), (r, g, b))


def rage(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))

            a = ((r + g + b)) // 3

            if a > 100:
                r, g, b = 255, 255, 255
            else:
                r, g, b = 255, 0, 0

            img.putpixel((i, j), (r, g, b))


def noice(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))

            a = ((r + g + b)) // 3

            rand = randint(-100, 100)
            r = r + (rand)
            g = g + (rand)
            b = b + (rand)

            img.putpixel((i, j), (r, g, b))


def rainbow(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))

            a = ((r + g + b)) // 3

            r = r + randint(10, 150)
            g = g + randint(10, 150)
            b = b + randint(10, 150)

            img.putpixel((i, j), (r, g, b))


def mate_four(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))

            a = ((r + g + b)) // 3

            i1 = img.width // 2
            f = img.height // 2
            if i < i1 and j < f:
                r = r + 50
                g = g + 50

            elif i < i1 and j > f:
                r = r + 50

            elif i > i1 and j < f:
                b = b + 50

            elif i > i1 and j > f:
                g = g + 50

            img.putpixel((i, j), (r, g, b))


def kek(img):
    crop = (img.width//2, 0, img.width, img.height)
    paste = (0, 0, img.width//2, img.height)
    crop_part = img.crop(crop)
    crop_part.save("crop_part.png")
    rotate_part = crop_part.transpose(Image.FLIP_LEFT_RIGHT)
    img.paste(rotate_part, paste)
    os.remove("crop_part.png")