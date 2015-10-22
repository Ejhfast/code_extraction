# How can I check for a blank image in Qt or PyQt?
im = Image.open('image.png')
bands = im.split()
isBlank = all(band.getextrema() == (255, 255) for band in bands)
