# How to create an array of image objects to use in a FOR loop?
images = [Image.open(os.path.join(path, 'my_image_%d.png' % x)) for x in range(1, 6)]
