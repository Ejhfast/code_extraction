# Faster way to loop through every pixel of an image in Python?
x, y = (image &gt; limit).nonzero()
vals = image[x, y]
