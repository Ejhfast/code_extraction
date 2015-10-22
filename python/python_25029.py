# Trying to convert a nested loop with two sequences into a lambda
(lambda words, rules: sum([[word[:-len(rule)]] if word.endswith(rule) else [] for word in words for rule in rules], []))(str_test.split(), stem_rules)
