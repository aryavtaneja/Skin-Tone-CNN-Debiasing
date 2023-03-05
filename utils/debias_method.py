import random

from PIL import Image


#input: a PIL Image object
#output: a PIL Image object
def M2_debias(input_img):
    img = input_img.convert("HSV")
        
    #apply random hue and value shifts
    hue = random.randint(-50, 50)
    value = random.randint(-50, 50)

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            h, s, v = img.getpixel((i, j))
            h += hue
            v += value
            img.putpixel((i, j), (h, s, v))

    img = img.convert("RGB")

    return img

def M4_debias(input_img):
    img = input_img.convert("HSV")
        
    #apply random hue, saturation and value shifts
    hue = random.randint(-50, 50)
    saturation = random.randint(-50, 50)
    value = random.randint(-50, 50)

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            h, s, v = img.getpixel((i, j))
            h += hue
            s += saturation
            v += value
            img.putpixel((i, j), (h, s, v))

    img = img.convert("RGB")

    return img
            