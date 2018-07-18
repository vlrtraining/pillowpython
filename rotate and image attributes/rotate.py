from PIL import Image,ImageDraw,ImageFont
'''im = Image.open("Digital marketing.png")
# The file format of the source file.
print("Image format:",im.format)
# The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
print("Image mode:",im.mode)
# Image size, in pixels. The size is given as a 2-tuple (width, height).
print("Image size:",im.size)
# Colour palette table, if any.
print("Image palete:",im.palette)'''



im = Image.open("Digital marketing.png")
image_rot_90 = im.rotate(90)
image_rot_90.save('image_rot_90.jpg')

image_rot_180 = im.rotate(180)
image_rot_180.save('image_rot_180.jpg')

image_rot_90_exp = im.rotate(90,expand=True)
image_rot_90_exp.save('image_rot_90_expand.jpg')
image_rot_18 = im.rotate(18)
image_rot_18.save('image_rot_18.jpg')
image_rot_90_exp = im.rotate(18,expand=True)
image_rot_90_exp.save('image_rot_18_expand.jpg')
