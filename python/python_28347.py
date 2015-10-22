# Convert only floating point numbers to int in list python
codes = [890.0,'JFR']
codes = [int(c) if isinstance(c, float) else c for c in codes]
