# List comprehension suggestion
even,odd = [],[]
for x in range(51): x%2 and even.append(x) or odd.append(x)
