# Get date and time when photo was taken from EXIF data using PIL
from PIL import Image
def get_date_taken(path):
    return Image.open(path)._getexif()[36867]
