# How can I create an empty n*m PNG file in Python?
from PIL import Image
image = Image.new('RGB', (n, m))
