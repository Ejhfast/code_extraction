# How does Django determine if an uploaded image is valid?
from PIL import Image
trial_image = Image.open(file)
trial_image.verify()
