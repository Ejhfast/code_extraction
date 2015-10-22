# Pandas Delete Row of Data where Index is String
mask = frame.index.map(lambda x: not isinstance(x, str))
frame = frame[mask]
