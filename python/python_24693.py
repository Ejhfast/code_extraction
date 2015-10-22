# Pygame - How to detect if sprites are in area?
for sprite in sprites:
    if something.distance(sprite) &lt; THRESHOLD:
        do_something_with_near_sprite(sprite)
