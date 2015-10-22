# PyGame - Plotting a Pixel and Printing out it's coordinates
elif event.type==pygame.MOUSEBUTTONDOWN and event.button==LEFT:
  print "You pressed the left mouse button at (%d,%d)" %event.pos
  screen.set_at((event.pos.x, event.pos.y), pygame.Color(255,0,0,255))
