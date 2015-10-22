# want to include specific characters in regex using python
x = raw_input("Enter string of length 7 to generate your scrabble helper: ")
p = re.compile('|'.join((c for c in x)))
