# Pulling contents from a Dictionary
for key, value in signatures.iteritems():
    if value is not None:
        mod_time, hash = value[1:]
