# How do I split these strings into arrays of strings?
c1 = "St. Louis       12             Cardinals"
words = [w.strip() for w in c1.split('  ') if w]
# words == ['St. Louis', '12', 'Cardinals']
