# Reading numeric keys from JSON file
with open('file1.json', 'r') as f:
    data2 = {tuple(int(x) for x in k.split(',')): v
        for (k, v) in json.load(f).items()}
