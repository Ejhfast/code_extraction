# How do I read a jpg or png from the windows clipboard in python and vice versa?
from PIL import ImageGrab
im = ImageGrab.grabclipboard()
im.save('somefile.png','PNG')
