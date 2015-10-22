# Integrate in sympy doesn't work for x*cos(n*pi*x/L), but DOES work for sqrt(1.)*x*cos(n*pi*x/L). Please see code snippets below
&gt;&gt;&gt; fs_coeff = integrate(x*cos(n*pi*x/L), (x, 0, L))
&gt;&gt;&gt; fs_coeff
Piecewise((L**2/2, n == 0), ((-1)**n*L**2/(pi**2*n**2) - L**2/(pi**2*n**2), True))
