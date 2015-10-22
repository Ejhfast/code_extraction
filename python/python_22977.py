# Dictionaries in Python and different ways of accessing it
for key in phonebook:
    if key.startswith("Sm"):
        print "Phone number of %s is %d" % (key, phonebook[key])
