from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
import os


path = './Images'
pathOut = '/edited'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.BoxBlur(radius=10)).convert('').rotate(-90)
    
    
    enhancer = ImageEnhance.Color(edit)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')



