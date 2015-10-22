# Find the min max and average of one column of data in python
with open("filename") as f:
    cols = [float(row.split("-")[-2]) for row in f.readlines()]
print min(cols), max(cols), sum(cols) / len(cols)
