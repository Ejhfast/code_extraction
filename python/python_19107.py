# Blitting a Pygame Tile-map Efficiently
for tile in tiles:
  if camera.viewport.contains(tile.rect):
    tile.draw()
