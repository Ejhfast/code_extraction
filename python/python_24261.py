# bayesian pca using PyMC
z = [pymc.MvNormal('z_%i' % i, np.zeros(dimZ), np.eye(dimZ)) for i in range(N)]
