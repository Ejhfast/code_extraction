# Entering precise degrees into python
import math
def radians_from_triple(deg, min=0, sec=0):
    return math.radians(deg + min * 60 ** -1 + sec * 60 ** -2)
