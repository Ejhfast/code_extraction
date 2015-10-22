# How to transpose a matrix without using numpy or zip (or other imports)
[[row[i] for row in data] for i in range(len(data[0]))]
