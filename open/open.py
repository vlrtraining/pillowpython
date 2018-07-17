from PIL import Image,ImageDraw,ImageFont
im = Image.open("praveen.jpg")
#im.show()

iwt = ImageDraw.Draw(im)
fnt = ImageFont.truetype('Amatic-Bold.ttf', 30)
fnt1 = ImageFont.truetype('Amatic-Bold.ttf', 40)
iwt.text((10,10), "Praveen angular trainer ",font=fnt, fill="red")
iwt.text((10,250), "9059868766 ",font=fnt1, fill="red")
im.save('praveen1.png')
im.show('praveen1.png')
