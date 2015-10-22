# Python PSD layers?
from PIL import Image, ImageSequence
im = Image.open("spam.psd")
layers = [frame.copy() for frame in ImageSequence.Iterator(im)]
