# Pythonic way to find elementa of a python list that are not contained in another python list
a = np.array(list_a)
b = np.array(list_b)
list_c = np.setdiff1d(b, a).tolist()
