# How to strip characters from the right side of every word in Python?
print " ".join(word.rstrip("!") for word in text.split())
