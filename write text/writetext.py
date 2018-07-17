from PIL import Image, ImageDraw,ImageFont
img = Image.new('RGB', (400, 500), color = (73, 109, 137))

iwt = ImageDraw.Draw(img)
fnt = ImageFont.truetype('Amatic-Bold.ttf', 50)
iwt.text((300,400), "VLR Training.in",font=fnt, fill=(255,255,0))

img.save('vlrtraining2.png')
img.show('vlrtraining2.png')

'''
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (400, 500), color = (73, 109, 137))

fnt = ImageFont.truetype('BAUHS93.ttf', 200)
d = ImageDraw.Draw(img)
d.text((10,10), "Hello world", font=fnt, fill=(255, 255, 0))

img.save('pil_text_font.png')
img.show('pil_text_font.png')
'''
