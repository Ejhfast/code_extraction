# PyAudio mixing multiple tracks and channels
In [4]: frame = np.zeros(1764, dtype=np.int16)
In [5]: %timeit np.mean([frame]*6, axis=0, dtype=np.int16)
1000 loops, best of 3: 1.01 ms per loop
