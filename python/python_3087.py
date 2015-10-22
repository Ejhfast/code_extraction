# Image bit manipulation in Python
r, g, b = im.split()              # split the image into separate color planes
im = Image.merge("RGB", (g, g, g))  # merge them back, using the green plane for each
