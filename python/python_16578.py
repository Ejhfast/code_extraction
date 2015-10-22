# np.where equivalent for multi-dimensional numpy arrays
[i[0] for i,v in np.ndenumerate(ar) if v == [5]]
=&gt; [0, 3, 4]
