# Load image from string
fstr = cStringIO.StringIO(simage)
pygame.image.load(fstr, namehint="somethinguseful")
