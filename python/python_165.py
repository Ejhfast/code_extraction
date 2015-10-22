# dropping trailing '.0' from floats
(str(i)[-2:] == '.0' and str(i)[:-2] or str(i) for i in ...)
