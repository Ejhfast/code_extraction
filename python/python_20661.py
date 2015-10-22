# Performance in numpy
b1 = np.all(frame &lt; NSigma2, axis=-1)
b2 = np.all(frame &gt; PSigma2, axis=-1)
frame[~(b1 | b2)] = 0
