# How to get line numbers of the snippets matching a regexp?
with open(somefile, 'r') as f:
     line_numbers = [n for n, line in enumerate(f) if re.search(someRegexp, line)]
