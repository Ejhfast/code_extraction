# How to make a surface with a transparent background in pygame
image = pygame.Surface([640,480], pygame.SRCALPHA, 32)
image = image.convert_alpha()
