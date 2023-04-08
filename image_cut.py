#import library

import random
from PIL import Image, ImageDraw

#alat za crtanje 

def line(image_path, output_path):
    image = Image.open('putanja do slike za obradu')
    draw = ImageDraw.Draw(image)
    colors = ["white"] #boja crte 

#loop, unutar definiranja for petlje, broj 60 kontrolira udaljenost izmedu crti,
#dok broj 10 pod draw.line(width=10) kontrolira sirinu crte
    
    for i in range(0,image.height,60):
        points = [(0,i), (image.width, i)]
        draw.line(points, width=10, fill="white", joint="none")

#specificiraj mjesto spremanja obradene slike         

    image.save('putanja spremanja')

if __name__ == "__main__":
    line("madison_county_bridge_2.jpg", "lines.jpg")
