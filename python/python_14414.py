# matlab function to python function conversion
def coord2index(hres, vres, hdiv, vdiv, x, y):
    return hdiv + x + 1, (-1) * y + vdiv
