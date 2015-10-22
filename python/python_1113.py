# Is there a way to split a string by every nth separator in Python?
span = 2
words = "this-is-a-string".split("-")
print ["-".join(words[i:i+span]) for i in range(0, len(words), span)]
