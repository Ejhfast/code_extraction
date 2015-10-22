# Dealing with zeros in numpy array normalization
nonzero = norms &gt; 0
x[nonzero] /= norms[nonzero]
