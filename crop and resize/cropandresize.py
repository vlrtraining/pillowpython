# import the Python Image processing Library
from PIL import Image
'''# Create an Image object from an Image
imageObject  = Image.open("Data-science.jpg")
# Crop the iceberg portion
cropped     = imageObject.crop((0,100,300,450))
# Save tah cropped image
cropped.save('Data-sciencecropped1.jpg')
# Display the crssopped portion
cropped.show()'''

imageObject  = Image.open("Data-science.jpg")
resizeimg     = imageObject.resize((500,300))
resizeimg.save('Data-scienceresize.jpg')
resizeimg.show()
