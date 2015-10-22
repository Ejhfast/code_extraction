# How do I enumerate() over a list of tuples in Python?
letters = [('a', 'A'), ('b', 'B')]
for i, (lowercase, uppercase) in enumerate(letters):
    print "Letter #%d is %s/%s" % (i, lowercase, uppercase)
