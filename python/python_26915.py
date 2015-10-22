# Reading in data with different delimiters in Python
with open('data.csv') as data:
    lines = [re.split(r'\s+|,', i.strip()) for i in data]
