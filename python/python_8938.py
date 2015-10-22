# Python PIL remove sections of an image based on its colour
source = im.split()
mask = source[2].point(lambda i: i &lt; 100 and 255)
im = Image.merge(im.mode, source)
