import random

from PIL import Image, ImageEnhance


# Input: a PIL Image object
# Output: a PIL Image object
def augment(input_img):
    #apply random pixelation, between 0-5%
    img = input_img.resize((int(img.size[0] * random.uniform(0.95, 1.05)), int(img.size[1] * random.uniform(0.95, 1.05))), Image.NEAREST)

    #apply random brightness and contrast shifts, between -15 to 15%
    brightness = random.uniform(-0.15, 0.15)
    contrast = random.uniform(-0.15, 0.15)

    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1 + brightness)

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1 + contrast)

    #apply random rotation between -3 to 3 degrees
    rotation = random.uniform(-3, 3)

    img = img.rotate(rotation)  

    #resize the image to 70x70
    img = img.resize((70, 70))   

    return img
