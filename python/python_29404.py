# Parsing Twitter JSONs in Python JSONDecodeError: Expecting value: line 2 column 1 (char 2)
for line in open('tweets.txt', 'r'):
    if line.strip():
        tweets.append(json.loads(line))
