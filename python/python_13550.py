# How do I make and assign a rect to a sprite in pygame?
s.image = pygame.image.load("sprite.png").convert() #load a sprite image
s.rect = b.image.get_rect() # set collision rectangle
