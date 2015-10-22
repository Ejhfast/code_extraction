# Regex patter for matching entire word if it have a ; in the word in python
s = 'the cat as;asas was wjdwi;qs at home'
res = ' '.join(w for w in s.split() if ';' not in w)
# the cat was at home
