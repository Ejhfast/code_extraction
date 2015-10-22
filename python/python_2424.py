# Fastest way to find the rotation of a vector
def after(u, v):
    # return sign of cross product
    return u[0]*v[1]&lt;u[1]*v[0]
