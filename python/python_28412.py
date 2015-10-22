# IndexError obstructing code from working with larger csv file
mode = (lambda ts: ts.value_counts(sort=True).index[0]
                   if len(ts.value_counts(sort=True)) else None)
