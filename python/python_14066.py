# Import RGB value of each pixel in an image to 1-D array
width, height = im.size
pixels = [pix[i, j] for i in range(width) for j in range(height)]
