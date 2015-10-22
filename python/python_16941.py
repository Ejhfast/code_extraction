# Determine arguments where two numpy arrays intersect in Python
&gt;&gt;&gt; np.arange(a.shape[0])[~np.in1d(a,b)].tolist()
  [0, 1, 3]
