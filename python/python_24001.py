# Determining the physical height of a gaussian curve (python)
def model(position, width, height):
    return  height * sqrt(2*pi) * width * scipy.stats.norm.pdf(x, position, width)
