# sort dates in python array
sorted(timestamps, key=lambda d: map(int, d.split('-')))
