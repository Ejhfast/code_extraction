# List comprehension in function arguments
def multicolor_message(msgs, colors=None):
  if colors is None:
    colors=[libtcod.white for x in len(msgs)]
