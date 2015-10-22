# Pythonic and concise way to construct this list?
scores = [read_score(f, normalize=True) for f in glob.glob(path)]
