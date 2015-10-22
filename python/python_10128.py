# Regular expression substitution Python
pattern = r'\b({})\b'.format('|'.join(map(re.escape, exclusionList)))
first_word = re.sub(pattern, '', first_word)
