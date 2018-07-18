from PIL import Image, ImageDraw
'''image = Image.open('birds.jpg')

image_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
image_flip.save('birdsFLIP_FLIP_TOP_BOTTOM.jpg')
'''
blank_image = Image.new('RGBA', (500, 500), 'green')
img_draw = ImageDraw.Draw(blank_image)
img_draw.rectangle((70, 50, 270, 200), outline='red', fill='blue')
img_draw.text((70, 250), 'Vlr training', fill='red')
blank_image.save('drawn_image1.png')
