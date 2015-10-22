# Change Int64Index to Index and dtype=int64 to dtype=object
for i in range(len(t.columns.levels)):
    if t.columns.levels[i].dtype == np.int64:
        t.columns.levels[i] = t.columns.levels[i].astype(np.float64)
