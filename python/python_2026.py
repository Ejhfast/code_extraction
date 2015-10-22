# Advanced Python list comprehension
[w for w in words if all([w[i] in chars[i] for i in range(len(w))])]
