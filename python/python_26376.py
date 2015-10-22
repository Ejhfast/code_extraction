# How to write a function in Python that can rotate an image (cImage)
from PIL import Image
im = Image.open(image)
im.rotate(90).show()
