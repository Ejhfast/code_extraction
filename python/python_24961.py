# Using PIL (Python Image Library) to detect image on screen
from PIL import ImageGrab
pil_img = ImageGrab.grab()
opencv_img = numpy.array(pil_img)
