#import library

import random
from PIL import Image, ImageDraw

#inputi
print("===========FUCKIN USELESS IMAGE PRINT COMPRESSOR============")
image_input = input("\n Enter image path:\n ----> ")
image_output= input("\n Enter image path output\n(if left blank, it will overwrite the input image):\n ----> ")
x = int(input("\n Enter the gap between lines: "))
y = int(input("\n Enter line width: "))

if (image_output == ""):
    image_output = image_input
#alat za crtanje 

def line(image_path, output_path):
    image = Image.open(image_input)
    draw = ImageDraw.Draw(image)
    colors = ["white"] #boja crte 

#loop: unutar definiranja for petlje, broj 60 kontrolira udaljenost izmedu crti,
#dok broj 10 pod draw.line(width=10) kontrolira sirinu crte
    
    for i in range(0,image.height,x):
        points = [(0,i), (image.width, i)]
        draw.line(points, width=y, fill="white", joint="none")

#specificiraj mjesto spremanja obradene slike         

    image.save(image_output)
    image = Image.open(image_output)

if __name__ == "__main__":
    line("madison_county_bridge_2.jpg", "lines.jpg")


