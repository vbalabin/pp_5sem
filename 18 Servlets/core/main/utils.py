from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile
import random
from core.settings import BASE_DIR
import os

HELLO = os.path.join(BASE_DIR, r"media\images\hello_world.png")

def change_photo():
    im = Image.new("RGB", (640,120), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    text = ImageDraw.Draw(im)
    font = ImageFont.truetype('venv\\Lib\\site-packages\\django\\contrib\\admin\static\\admin\\fonts\\Arial.ttf', size=72)
    text.text(
        (100,28),
        "Hello world",
        font= font,
        fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255))

    )
    im.save(fp=HELLO)
    return r"media\images\hello_world.png"



if __name__ == '__main__':
    change_photo()