import random

from PIL import Image


#input: a PIL Image object
#output: a PIL Image object
def debias(input_img):
    img = input_img.convert("HSV")
        
    #apply random hue and value shifts
    hue = random.randint(-15, 15)
    value = random.randint(-50, 15)

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            h, s, v = img.getpixel((i, j))
            h += hue
            v += value
            img.putpixel((i, j), (h, s, v))

    img = img.convert("RGB")

    return img
            