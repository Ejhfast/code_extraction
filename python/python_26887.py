# why does resizing image in Pillow-python remove Image.format?
image = Image.open("image_file.jpg") #old image object
resized_image = image.resize([100,200],PIL.Image.ANTIALIAS)
resized_image.format = image.format # original image extension
