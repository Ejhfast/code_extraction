# Create all sequences from the first item within a list
prefixes = [your_list[:end] for end in xrange(1, len(your_list) + 1)]
