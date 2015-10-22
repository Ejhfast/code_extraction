# Split string words in pairs for all side by side words
from itertools import izip
[' '.join(pair) for pair in izip(words[:-1], words[1:])]
