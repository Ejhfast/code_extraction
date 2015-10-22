# Implementation of derivatives of Jacobi theta function
def jtheta_dq(n, z, q):
    # cf. http://functions.wolfram.com/EllipticFunctions/EllipticTheta2/13/01/0002/
    return -mpmath.jtheta(n, z, q, 2)/(4*q)
