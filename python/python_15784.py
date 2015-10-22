# count occurrences of timeframes in a list
from collections import Counter
counts = Counter(time[:2]+'00' for time in times)
