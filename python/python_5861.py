# how to invoke another function when sprites collide in pygame
hitApples = pygame.sprite.spritecollide(snake, apple_list, True)
if hitApples:
    callback()
