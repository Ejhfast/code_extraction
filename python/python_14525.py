# python - string match only whole words
re.search(r'\b' + re.escape(' '.join(query)) + r'\b', ' '.join(line)) is not None
