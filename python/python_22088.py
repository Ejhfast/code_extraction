# Sympy - Comparing two string inputs causes unexpected result
if (arg1.as_numer_denom() == arg2.as_numer_denom() and
    simplify(arg1 - arg2) == 0):
