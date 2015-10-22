# Transition markov matrix with numpy
matrix = np.random.randint(300, size=(20, 20))
transition_matrix = matrix / matrix.sum(axis=1).astype(float)
