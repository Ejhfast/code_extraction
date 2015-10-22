# Python: Reading Fortran Binary file using numpy or scipy
with open('filepath','r') as f:
    header = np.fromfile(f, dtype=np.int, count=number_of_integers)
    data = np.fromfile(f, dtype=np.float32)
