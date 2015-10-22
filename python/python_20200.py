# Fast way to apply function elementwise to a numpy array
set((np.convolve(v, longtuple, 'valid') &gt;&gt; k &amp; 1).tostring() for v in itertools.product([0,1], repeat = m))
