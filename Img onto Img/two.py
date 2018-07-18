from PIL import Image,ImageDraw,ImageFont
'''
image = Image.open('Digital marketing.png')
logo = Image.open('vlrtra.jpg')
image_copy = image.copy()
#image_copy.save('rrr.jpg')
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
image_copy.paste(logo, position)
image_copy.save('pasted_image.jpg')#Pasting an Image onto Another Image
'''
image = Image.open('Digital marketing.png')
logo = Image.open('vlrtra.jpg')
image_copy = image.copy()
image_copy.save('dm2.jpg')
position = (((int(image.width /2))), ((int(image.height /2))))
image.paste(logo, position)
image.save('with logo.jpg')
#Pasting an Image onto Another Image
