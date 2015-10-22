# How to exactly solve quadratic equations with large integer coefficients (over integers)?
a, b, c = 2, 616872928410303123, -1850618785230909388
x = Symbol('x')
int(max(solve(a*x**2 + b*x + c, x)))
