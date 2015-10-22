# double list comprehension
terms = set([" ".join(words[j:j + len(words) - i])
               for i in xrange(len(words)) for j in xrange(len(words))])
