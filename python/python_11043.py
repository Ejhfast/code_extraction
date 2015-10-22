# condensing serial for loops
centers_x = [np.mean([q[0] for q in coordinates if q[-1]==n]) for n in range(3)]
