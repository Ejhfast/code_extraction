# Find global min values from sub-sub-lists of different lengths
map(lambda x: min(map(min, x)), zip(*a))
