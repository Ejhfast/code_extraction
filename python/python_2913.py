# How I can develop a screen-capture tool in Python
from PIL import ImageGrab
ImageGrab.grab().save("screenshot.jpg", "JPEG")
