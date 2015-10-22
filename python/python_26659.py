# why return np.random.normal(10 - 1. / (x + 0.1), 0.5) works
np.random.normal(np.zeros(8), 0.5) + 10 - 1. / (x + 0.1)
