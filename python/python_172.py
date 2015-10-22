# Resize image in Python without losing EXIF data
import jpeg
jpeg.setExif(jpeg.getExif('foo.jpg'), 'foo-resized.jpg')
