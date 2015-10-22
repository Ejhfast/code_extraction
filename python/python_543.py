# Convert list of lists to delimited string
lists = [['dog', 1], ['cat', 2, 'a'], ['rat', 3, 4], ['bat', 5]]
result = "\n".join("\t".join(map(str,l)) for l in lists)
