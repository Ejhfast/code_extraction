# Set of dictionary values python
d = {'ABCS': ['12', '12', '113', '12']}
print {k: list(set(v)) for k,v in d.items()}
{'ABCS': ['12', '113']}
