# Sets vs. Regex for string lookup, which is more scalable?
s = set(big_list)
sum(1 for x in re.finditer(r'\b\w+\b',sentence) if x.group() in s)
