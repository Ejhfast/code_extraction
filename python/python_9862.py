# Append barcode images to docx file using pybarcode ImageWriter and docx module
from PIL import Image
im = Image.open("barcode.png")
im.resize((480,320)).save("barcode_resized.png")
