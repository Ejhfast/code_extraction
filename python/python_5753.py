# Checking compatible total orders given by a Python list
def compat5(L1, L2):
    z = zip(L1, L2)
    return not any(j1&lt;k1 and j2&gt;k2 for j1,j2 in z for k1,k2 in z)
