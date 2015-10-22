# Checking 2-dimensional array (like eight queens puzzle)
def collision(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2)
