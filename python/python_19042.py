# Inaccurate Rectangular Collision Detection in python
def standardize(p1, p2):
    xs, ys = zip(p1, p2)
    return (max(xs), max(ys)), (min(xs), min(ys))
