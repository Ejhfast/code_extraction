# Pythonic method of increasing two counters depending on boolean check
from collections import Counter
counts = Counter(d.check(word) for (word,pos) in tokenizer(text))
good, bad = counts[True], counts[False]
