# Seeing if a list exists within another list?
any(a[i:i + len(b)] == b for i in range(len(a) - len(b) + 1))
