# Use of global dictionary to create variables
files = {f: np.loadtxt(f) for f in glob.glob("*.txt")}
