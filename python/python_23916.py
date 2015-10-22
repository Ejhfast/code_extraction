# Finding same values in a row of csv in python
data = np.genfromtxt(filepath, names=True, dtype=None)
idx = np.abs(data['Chan1'] - data['Chan2'])&lt;1
print data[idx]
