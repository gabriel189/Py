#import library

import random
from PIL import Image, ImageDraw

image_input = ""
while image_input != "N":

#inputi
    print("===========FUCKIN USELESS IMAGE CROP============")
    image_input = input("\n Enter image path:\n ----> ")
    image_output= input("\n Enter image path output\n(if left blank, it will overwrite the input image):\n ----> ")


    if (image_output == ""):
        image_output = image_input
#alat za crtanje 


    image = Image.open(image_input)
    width, height = image.size

    print(width, height)
    x = width / 3
    y = x * 2
    z = (height - y) / 2
    left = 0
    top = z
    right = width
    bottom = height - z
    image = image.crop((left, top, right, bottom))

    
   

#specificiraj mjesto spremanja obradene slike         

    image.save(image_output)
    image = Image.open(image_output)



