# python convert 12 bit image encoded in a string to 8 bit png
#shifts by 4 bits and converts to 8-bit image
img = img.point(lambda i: i * 16, "L")
