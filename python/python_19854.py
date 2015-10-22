# defaultdict tuple of lists
foo = defaultdict(lambda: ([], []))
foo['key1'][0].append('value')
