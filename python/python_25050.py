# How to do a sum of sums of the square of sum of sums?
E = np.einsum('uk, vl, xk, yl, xy, kl-&gt;uvxy', Fu, Fv, Fx, Fy, P, B)
E1 = np.einsum('uvxy-&gt;uv', E)
E2 = np.einsum('uvxy-&gt;uv', np.square(E))
