from PIL import Image,ImageDraw,ImageFont
'''
image = Image.open('Data-science.jpg')
image.save('Data-science.png')
image.show()
'''
image = Image.open('Data-science.png')
image.save('Data-science1.jpg')
image.show()

image = Image.open('asdf.jpg')
greyscale_image = image.convert('L')
greyscale_image.save('greyscale_asdf.jpg')
greyscale_image.show()
cmyk_image = image.convert('CMYK')
cmyk_image.save('cmyk_image.jpg')
cmyk_image.show()
RGB_image = image.convert('RGB')
RGB_image.save('rgb_image.jpg')
RGB_image.show()

'''


'''
