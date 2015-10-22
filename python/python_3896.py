# In Python's PIL, how do I change the quality of an image?
from PIL import Image
im = Image.open("C:\Users\Public\Pictures\Sample Pictures\Jellyfish.jpg")
im.save("C:\Users\Public\Pictures\Sample Pictures\Jellyfish_compressed.jpg", quality=10)
